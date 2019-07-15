from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template
from ask_sdk_model.dialog import DelegateDirective

from alexa.request_handler.buildin.fallback import fallback_request
from core.models import Scenario


def in_progress_choose_sceanrio_request(handler_input, minus_points):
    session_attributes = handler_input.attributes_manager.session_attributes
    if not session_attributes.get('scenario'):
        current_intent = handler_input.request_envelope.request.intent
        return handler_input.response_builder.add_directive(DelegateDirective(updated_intent=current_intent)).response
    else:
        return fallback_request(handler_input, minus_points)


def choose_sceanrio_request(handler_input, minus_points):
    """Handler for Choose Scenario Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes

    if not session_attributes.get('scenario'):
        slots = handler_input.request_envelope.request.intent.slots
        scenario_slot = slots.get('scenario').value if slots.get('scenario') else None
        try:
            scenario = Scenario.objects.get(name__contains=scenario_slot) if scenario_slot else None
            session_attributes['scenario'] = scenario.id
            speech_text = get_template('skill/close_box.html').render()
            return handler_input.response_builder.speak(
                speech_text
            ).set_card(
                SimpleCard(
                    f'Szenario: {scenario.name}',
                    BeautifulSoup(speech_text, features="html.parser").text
                )
            ).set_should_end_session(
                False
            ).response
        except RuntimeError:
            fallback_request(handler_input, minus_points)
    else:
        return fallback_request(handler_input, minus_points)
