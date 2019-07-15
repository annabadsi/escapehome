from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from core.models import Scenario


def navigate_menu_request(handler_input):
    """Handler for Help Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    slots = handler_input.request_envelope.request.intent.slots
    scenario_slot = slots.get('scenario').value if slots.get('scenario') else None
    scenario = Scenario.objects.get(name__contains=scenario_slot) if scenario_slot else None
    riddle = scenario.riddles.first() if scenario else None

    if scenario:
        session_attributes['scenario'] = scenario.id
        session_attributes['riddle'] = scenario.riddles.first().id
        session_attributes['counter'] = 0
        session_attributes['score'] = 0

    speech_text = get_template('skill/navigate_menu.html').render(
        {
            'scenario': scenario,
            'riddle': riddle,
            'scenarios': Scenario.objects.all(),
        }
    )

    return handler_input.response_builder.speak(
        speech_text
    ).ask(
        speech_text
    ).set_card(
        SimpleCard(
            "Du brauchst Hilfe?",
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).response
