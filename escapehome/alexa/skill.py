import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard

from alexa.skills.scenario import choose_scenario
from core.models import Scenario

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    speech_text = (
        f'Willkommen zu <lang xml:lang="en-US">Escape Home</lang>!'
        f'<p>Es gibt {Scenario.objects.count()} verschiedene Szenarien:</p>'
        f'{" oder ".join(Scenario.objects.values_list("name", flat=True))}'
        f'<p>Welches möchtest du spielen?</p>'
    )

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Willkommen",
            speech_text
        )
    ).set_should_end_session(
        False
    ).response


@sb.request_handler(can_handle_func=is_intent_name("ChooseScenario"))
def choose_sceanrio_intent_handler(handler_input):
    """Handler for Choose Scenario Intent."""

    slots = handler_input.request_envelope.request.intent.slots
    speech_text = choose_scenario(slots.get("scenario").value)

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Wähle ein Szenario",
            speech_text
        )
    ).set_should_end_session(
        True
    ).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    speech_text = "Wähle ein Szenarium aus!"

    return handler_input.response_builder.speak(
        speech_text
    ).ask(
        speech_text
    ).set_card(
        SimpleCard(
            "Hilfe",
            speech_text
        )
    ).response


@sb.request_handler(
    can_handle_func=lambda handler_input:
    is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)
)
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    speech_text = (
        f'<say-as interpret-as="interjection">ade</say-as>'
        f'<p>ich warte hier auf dich.</p>'
    )

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Auf Wiedersehen",
            speech_text
        )
    ).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale, so it is safe to deploy on any locale."""
    speech = "Ich weiß nicht was du meinst."
    reprompt = "Wähle ein Szenario aus."
    handler_input.response_builder.speak(speech).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and respond with custom message."""
    logger.error(exception, exc_info=True)
    speech_text = f'<say-as interpret-as="interjection">ähm</say-as>, es gab wohl ein Problem!'

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response


skill = sb.create()
