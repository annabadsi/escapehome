from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from api.views import create_json
from core.models import Scenario, ActiveScenario


def launch_request(handler_input):
    """Handler for Skill Launch."""
    session_attributes = handler_input.attributes_manager.session_attributes

    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario, created = ActiveScenario.objects.get_or_create(user=user)

    session_attributes['box'] = True

    # new game
    if created or not active_scenario.scenario:
        speech_text = get_template('skill/welcome.html').render(
            {'scenarios': Scenario.objects.all()}
        )

    # continue game
    else:
        session_attributes['scenario'] = active_scenario.scenario.id
        session_attributes['riddle'] = active_scenario.riddle.id
        session_attributes['counter'] = active_scenario.state
        session_attributes['score'] = active_scenario.score

        create_json(active_scenario.riddle)

        speech_text = get_template('skill/welcome_back.html').render(
            {'active_scenario': active_scenario}
        )

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response
