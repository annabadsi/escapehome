from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from core.models import Scenario


def close_box_start_game_request(handler_input):
    """Handler to close box and start the game"""
    counter = 0
    slots = handler_input.request_envelope.request.intent.slots
    session_attributes = handler_input.attributes_manager.session_attributes
    scenario_slot = slots.get('scenario').value if slots.get('scenario') else None
    scenario = Scenario.objects.get(name__contains=scenario_slot) if scenario_slot else None

    speech_text = get_template('skill/scenario.html').render(
        {'scenario': scenario, 'riddle': scenario.riddles.first()}
    )

    if scenario:
        session_attributes['scenario'] = scenario.id
        session_attributes['counter'] = counter
        session_attributes['riddle'] = scenario.riddles.first().id
        session_attributes['score'] = 0

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            f'{counter + 1}. Rästel für Szenario: {scenario.name}',
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        False
    ).response
