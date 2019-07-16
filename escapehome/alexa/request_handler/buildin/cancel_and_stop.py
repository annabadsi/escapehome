from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from api.views import box_command_to_json
from core.models import Scenario, ActiveScenario, Command


# TODO: nicht nur beim Beenden speichern sondern nach jedem Request? Falls bei Fehler nicht gespeicht wird

def cancel_and_stop_request(handler_input, quit_minus_points):
    """Single handler for Cancel and Stop Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    in_game = False

    if not session_attributes.get('box'):
        in_game = True

        # get session attributes
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes['riddle'])
        score = session_attributes['score']
        counter = session_attributes['counter']

        # reopen box
        box_command_to_json(Command.objects.get(name='modbus box öffnen'), user)
        session_attributes['box'] = True
        score += quit_minus_points

        # save attributes in database
        active_scenario = ActiveScenario.objects.get(user=user)
        active_scenario.scenario = scenario
        active_scenario.riddle = riddle
        active_scenario.score = score
        active_scenario.state = counter
        active_scenario.save()

    speech_text = get_template('skill/cancel_and_stop.html').render({'ingame': in_game})

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Auf Wiedersehen",
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        True
    ).response
