import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import DialogState
from ask_sdk_model.dialog import DelegateDirective

from alexa.request_handler.choose_scenario import choose_sceanrio_request
from alexa.request_handler.close_box_start_game import close_box_start_game_request
from alexa.request_handler.helper.cancel_and_stop import cancel_and_stop_request
from alexa.request_handler.helper.exception import exception_request
from alexa.request_handler.helper.fallback import fallback_request
from alexa.request_handler.helper.help import help_request
from alexa.request_handler.helper.navigate_menu import navigate_menu_request
from alexa.request_handler.launch import launch_request
from alexa.request_handler.pose_riddle import pose_riddle_request

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MINUS_POINTS = -1


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    return launch_request(handler_input)


@sb.request_handler(can_handle_func=lambda i: is_intent_name('ChooseScenario')(
    i) and i.request_envelope.request.dialog_state == DialogState.COMPLETED)
def choose_sceanrio_intent_handler(handler_input):
    """Handler for Choose Scenario Intent."""
    return choose_sceanrio_request(handler_input, MINUS_POINTS)


@sb.request_handler(can_handle_func=is_intent_name("CloseBoxStartGame"))
def close_box_start_game_intent_handler(handler_input):
    """Handler to close box and start the game"""
    return close_box_start_game_request(handler_input)


@sb.request_handler(can_handle_func=lambda i: is_intent_name('ChooseScenario')(
    i) and i.request_envelope.request.dialog_state != DialogState.COMPLETED)
def in_progress_choose_sceanrio_intent_handler(handler_input):
    current_intent = handler_input.request_envelope.request.intent
    return handler_input.response_builder.add_directive(DelegateDirective(updated_intent=current_intent)).response


@sb.request_handler(can_handle_func=is_intent_name("PoseRiddle"))
def pose_riddle_intent_handler(handler_input):
    """Handler for Pose Riddle Intent."""
    return pose_riddle_request(handler_input, MINUS_POINTS)


@sb.request_handler(can_handle_func=is_intent_name("NavigateMenu"))
def navigate_menu_intent_intent_handler(handler_input):
    """Handler for Help Intent."""
    return navigate_menu_request(handler_input)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    return help_request(handler_input, MINUS_POINTS)


@sb.request_handler(
    can_handle_func=lambda handler_input:
    is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)
)
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    cancel_and_stop_request(handler_input)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """Fallback Handler"""
    return fallback_request(handler_input, MINUS_POINTS)


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # TODO: do something (tritt zB. auf wenn handler methode nicht gefunden wird)
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and respond with custom message."""
    exception_request(handler_input, exception, logger)


skill = sb.create()
