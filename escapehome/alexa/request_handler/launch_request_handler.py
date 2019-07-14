from core.models import Scenario, ActiveScenario
from hue.lights import Hue


def launch_request(handler_input):
    """Handler for Skill Launch."""
    session_attributes = handler_input.attributes_manager.session_attributes

    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario, created = ActiveScenario.objects.get_or_create(user=user)

    if created or not active_scenario.scenario:
        speech_text = get_template('skill/welcome.html').render(
            {'scenarios': Scenario.objects.all()}
        )

    else:
        session_attributes['scenario'] = active_scenario.scenario.id
        session_attributes['riddle'] = active_scenario.riddle.id
        session_attributes['counter'] = active_scenario.state
        session_attributes['score'] = active_scenario.score

        # TODO: Das übernimmt der PI dann
        if active_scenario.riddle.commands.all():
            execute_command(active_scenario.riddle.commands.all())

        speech_text = get_template('skill/welcome_back.html').render(
            {'active_scenario': active_scenario}
        )

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        False
    ).response