from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template
from ask_sdk_model.dialog import DelegateDirective

from alexa.request_handler.buildin.cancel_and_stop import cancel_and_stop_request
from alexa.request_handler.buildin.fallback import fallback_request
from core.models import Scenario, ActiveScenario


def in_progress_choose_sceanrio_request(handler_input, minus_points, quit_minus_points):
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)

    # if box was opened in game
    if not session_attributes.get('box') and active_scenario.box:
        return cancel_and_stop_request(handler_input, quit_minus_points)

    # only ask how many persons will participate if scenario is selected
    if not session_attributes.get('scenario'):
        try:
            slots = handler_input.request_envelope.request.intent.slots
            scenario_slot = slots.get('scenario').value if slots.get('scenario') else None
            Scenario.objects.get(other_names__contains=scenario_slot) if scenario_slot else None
        except Scenario.DoesNotExist:
            return fallback_request(handler_input, minus_points, quit_minus_points)

        current_intent = handler_input.request_envelope.request.intent
        return handler_input.response_builder.add_directive(DelegateDirective(updated_intent=current_intent)).response
    else:
        return fallback_request(handler_input, minus_points, quit_minus_points)


def choose_sceanrio_request(handler_input, minus_points, quit_minus_points):
    """Handler for Choose Scenario Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    slots = handler_input.request_envelope.request.intent.slots
    active_scenario = ActiveScenario.objects.get(user=user)

    # if box was opened in game
    if not session_attributes.get('box') and active_scenario.box:
        return cancel_and_stop_request(handler_input, quit_minus_points)

    if slots.get('players'):
        user_input = (slots.get('players').value)
        try:
            number_of_players = int(user_input)
        except ValueError:
            number_of_players = 0
    else:
        number_of_players = 0

    session_attributes['players'] = number_of_players

    # if scenario set in session
    if not session_attributes.get('scenario'):
        # save players
        try:
            scenario = Scenario.objects.get(
                other_names__contains=slots.get('scenario').value if slots.get('scenario') else None
            )
            session_attributes['scenario'] = scenario.id
            speech_text = get_template('skill/close_box.html').render()
            return handler_input.response_builder.speak(
                speech_text
            ).set_card(
                SimpleCard(
                    f'Spiel Vorbereitungen',
                    BeautifulSoup(speech_text, features="html.parser").text
                )
            ).set_should_end_session(
                False
            ).response
        except Scenario.DoesNotExist as e:
            print('Scenario.DoesNotExist: ', e)
            return fallback_request(handler_input, minus_points, quit_minus_points)
        except ValueError as e:
            print('ValueError: ', e)
            return fallback_request(handler_input, minus_points, quit_minus_points)
    else:
        return fallback_request(handler_input, minus_points, quit_minus_points)
