import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import DialogState

from alexa.request_handler.intents.choose_scenario import choose_sceanrio_request, in_progress_choose_sceanrio_request
from alexa.request_handler.intents.close_box_start_game import close_box_start_game_request
from alexa.request_handler.buildin.cancel_and_stop import cancel_and_stop_request
from alexa.request_handler.buildin.exception import exception_request
from alexa.request_handler.buildin.fallback import fallback_request
from alexa.request_handler.buildin.help import help_request
from alexa.request_handler.launch import launch_request
from alexa.request_handler.intents.pose_riddle import pose_riddle_request

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MINUS_POINTS = -1
QUIT_MINUS_POINTS = -10


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    return launch_request(handler_input)


@sb.request_handler(can_handle_func=lambda i: is_intent_name('ChooseScenario')(
    i) and i.request_envelope.request.dialog_state != DialogState.COMPLETED)
def in_progress_choose_sceanrio_intent_handler(handler_input):
    return in_progress_choose_sceanrio_request(handler_input, MINUS_POINTS, QUIT_MINUS_POINTS)


@sb.request_handler(can_handle_func=lambda i: is_intent_name('ChooseScenario')(
    i) and i.request_envelope.request.dialog_state == DialogState.COMPLETED)
def choose_sceanrio_intent_handler(handler_input):
    """Handler for Choose Scenario Intent."""
    return choose_sceanrio_request(handler_input, MINUS_POINTS, QUIT_MINUS_POINTS)


@sb.request_handler(can_handle_func=is_intent_name("CloseBoxStartGame"))
def close_box_start_game_intent_handler(handler_input):
    """Handler to close box and start the game"""
    return close_box_start_game_request(handler_input, MINUS_POINTS, QUIT_MINUS_POINTS)


@sb.request_handler(can_handle_func=is_intent_name("PoseRiddle"))
def pose_riddle_intent_handler(handler_input):
    """Handler for Pose Riddle Intent."""
    return pose_riddle_request(handler_input, MINUS_POINTS, QUIT_MINUS_POINTS)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    return help_request(handler_input, MINUS_POINTS, QUIT_MINUS_POINTS)


@sb.request_handler(
    can_handle_func=lambda handler_input:
    is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)
)
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    return cancel_and_stop_request(handler_input, QUIT_MINUS_POINTS)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """Fallback Handler"""
    return fallback_request(handler_input, MINUS_POINTS, QUIT_MINUS_POINTS)


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest")) # TODO name richtig?
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # TODO: do something (tritt zB. auf wenn handler methode nicht gefunden wird)
    print("SESSION ENDED method called")
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and respond with custom message."""
    return exception_request(handler_input, exception, logger)


skill = sb.create()
