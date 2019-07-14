from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from alexa.request_handler.helper.fallback import fallback_request
from core.models import Scenario


def choose_sceanrio_request(handler_input, minus_points):
    """Handler for Choose Scenario Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes

    #if not session_attributes.get('scenario'):
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
    #elif box?
    #else:
    #    return fallback_request(handler_input, minus_points)
