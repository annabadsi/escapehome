import logging

from bs4 import BeautifulSoup
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import DialogState
from ask_sdk_model.dialog import DelegateDirective
from ask_sdk_model.ui import SimpleCard
from django.template.loader import get_template

from core.models import Scenario, ActiveScenario
from hue.lights import Hue

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MINUS_POINTS = -1


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    session_attributes = handler_input.attributes_manager.session_attributes

    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario, created = ActiveScenario.objects.get_or_create(user=user)

    if created or not active_scenario.scenario:
        speech_text = get_template('skill/welcome.html').render(
            {'scenarios': Scenario.objects.all()}
        )

    else:
        session_attributes['scenario'] = active_scenario.scenario.id
        session_attributes['riddle'] = active_scenario.riddle.id
        session_attributes['counter'] = active_scenario.state
        session_attributes['score'] = active_scenario.score

        # TODO: Das übernimmt der PI dann
        if active_scenario.riddle.commands.all():
            execute_command(active_scenario.riddle.commands.all())

        speech_text = get_template('skill/welcome_back.html').render(
            {'active_scenario': active_scenario}
        )

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        False
    ).response


@sb.request_handler(can_handle_func=lambda i: is_intent_name('ChooseScenario')(
    i) and i.request_envelope.request.dialog_state == DialogState.COMPLETED)
def choose_sceanrio_intent_handler(handler_input):
    """Handler for Choose Scenario Intent."""
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


@sb.request_handler(can_handle_func=lambda i: is_intent_name('ChooseScenario')(
    i) and i.request_envelope.request.dialog_state != DialogState.COMPLETED)
def in_progress_choose_sceanrio_intent_handler(handler_input):
    current_intent = handler_input.request_envelope.request.intent

    return handler_input.response_builder.add_directive(
        DelegateDirective(
            updated_intent=current_intent
        )).response


@sb.request_handler(can_handle_func=is_intent_name("PoseRiddle"))
def pose_riddle_intent_handler(handler_input):
    """Handler for Pose Riddle Intent."""
    slots = handler_input.request_envelope.request.intent.slots
    session_attributes = handler_input.attributes_manager.session_attributes
    set_should_end_session = False
    next_riddle = None

    # slots
    answer = slots.get("answer").value if slots.get("answer").value else slots.get("number").value

    # attributes
    counter = session_attributes['counter']
    scenario = Scenario.objects.get(id=session_attributes['scenario'])
    riddle = scenario.riddles.get(id=session_attributes['riddle'])
    score = session_attributes['score']

    if answer in riddle.solution.lower().split(', '):
        # Richtige Antwort
        counter += 1
        score += riddle.points
        if counter == scenario.riddles.count():
            # Gewonnen: alle Rätsel beantwortet
            set_should_end_session = True

            # TODO: active sceanario nicht löschen!
            user = handler_input.request_envelope.context.system.user.user_id
            ActiveScenario.objects.get(user=user).delete()
        else:
            # Gehe zum nächsten Rätsel
            next_riddle = scenario.riddles.all()[counter]

            # TODO: Das übernimmt der PI dann
            if next_riddle.commands.all():
                execute_command(next_riddle.commands.all())

            session_attributes['riddle'] = scenario.riddles.all()[counter].id
    else:
        # Falsche Antwort
        score += MINUS_POINTS

    speech_text = get_template('skill/riddle.html').render(
        {
            'score': score,
            'counter': counter,
            'scenario': scenario,
            'riddle': riddle,
            'next_riddle': next_riddle,
            'correct': answer in riddle.solution.lower().split(', '),
        }
    )

    session_attributes['counter'] = counter
    session_attributes['score'] = score

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            f'{counter + 1}. Rästel',
            f'Deine Antwort für die Frage: {riddle.task} lautete "{answer}"\n\n.'
            f'{BeautifulSoup(speech_text, features="html.parser").text}'
        )
    ).set_should_end_session(
        set_should_end_session
    ).response


@sb.request_handler(can_handle_func=is_intent_name("NavigateMenu"))
def navigate_menu_intent_intent_handler(handler_input):
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


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    riddle = None

    if session_attributes.get('scenario'):
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
        session_attributes['score'] += MINUS_POINTS

    speech_text = get_template('skill/help.html').render(
        {
            'scenario': session_attributes.get('scenario'),
            'scenarios': Scenario.objects.all(),
            'riddle': riddle,
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


@sb.request_handler(
    can_handle_func=lambda handler_input:
    is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)
)
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes

    # TODO: nicht nur beim Beenden speichern sondern nach jedem Request? Falls bei Fehler nicht gespeicht wird
    # attributes
    scenario = Scenario.objects.get(id=session_attributes['scenario'])
    riddle = scenario.riddles.get(id=session_attributes['riddle'])
    score = session_attributes['score']
    counter = session_attributes['counter']

    # in model speichern
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)
    active_scenario.scenario = scenario
    active_scenario.riddle = riddle
    active_scenario.score = score
    active_scenario.state = counter
    active_scenario.save()

    speech_text = get_template('skill/cancel_and_stop.html').render()

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Auf Wiedersehen",
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale, so it is safe to deploy on any locale."""
    session_attributes = handler_input.attributes_manager.session_attributes

    speech_text = get_template('skill/exception.html').render(
        {
            'scenario': session_attributes.get('scenario'),
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
            BeautifulSoup(speech_text, features="html.parser").text)
    ).response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and respond with custom message."""
    session_attributes = handler_input.attributes_manager.session_attributes

    # TODO: nicht nur beim Beenden speichern sondern nach jedem Request? Falls bei Fehler nicht gespeicht wird
    # attributes
    scenario = Scenario.objects.get(id=session_attributes.get('scenario'))
    riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
    score = session_attributes['score']
    counter = session_attributes['counter']

    # in model speichern
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)
    active_scenario.scenario = scenario
    active_scenario.riddle = riddle
    active_scenario.score = score
    active_scenario.state = counter
    active_scenario.save()

    logger.error(exception, exc_info=True)

    speech_text = get_template('skill/exception.html').render()

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response


def execute_command(commands):
    h = Hue()
    for command in commands:
        for action in command.actions.all().order_by('orderedaction'):
            func = getattr(h, action.function)
            lights = command.devices.values_list('lamp__lamp_id', flat=True)
            h.lights = lights
            func(**eval(action.parameters))


skill = sb.create()
