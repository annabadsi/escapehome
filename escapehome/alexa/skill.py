import logging

from bs4 import BeautifulSoup
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import DialogState
from ask_sdk_model.dialog import DelegateDirective
from ask_sdk_model.ui import SimpleCard

from alexa.skills.scenario import choose_scenario
from core.models import Scenario, ActiveScenario

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
        # TODO: Würde ich nochmal umschreiben (Simplecard ist gleich, Join geht auch mit einem Listenelement, nur den einen Satz austauschen
        # TODO: Erfüllt nicht den Sinn von Dialog!
        if Scenario.objects.count() > 1:
            speech_text = (
                f'Willkommen zu <lang xml:lang="en-US">Escape Home</lang>! '
                f'<p>Es gibt {Scenario.objects.count()} verschiedene Szenarien:</p> '
                f'{" oder ".join(Scenario.objects.values_list("name", flat=True))} '
                f'<p>Welches möchtest du spielen?</p>'
            )

            card = SimpleCard(
                'Willkommen - Szeanrio Auwahl',
                'Wähle aus den vorgebenen Spielen aus:\n'
                f'{", ".join(Scenario.objects.values_list("name", flat=True))}'
            )
        else:
            scenario = Scenario.objects.all()[0]

            speech_text = (
                f'Willkommen zu <lang xml:lang="en-US">Escape Home</lang>! '
                f'<p> Es gibt das Szenario {scenario.name}.</p>'
                f'<p> Möchtest du es spielen? Dann sag jetzt: {scenario.name}</p>'
            )

            card = SimpleCard(
                'Willkommen - Szeanrio Auwahl',
                'Wähle aus den vorgebenen Spielen aus:\n'
                f'{", ".join(Scenario.objects.values_list("name", flat=True))}'
            )

    else:
        speech_text = (
            f'<p>Willkommen zurück!</p>'
            f'<p>Das Spiel {active_scenario.scenario.name} wird fortgesetzt.</p>'
            f'<p>Dein zuletzt gespieltes noch ungelöstes Rätsel lautet: {active_scenario.riddle.task}</p>'
        )

        session_attributes['scenario'] = active_scenario.scenario.id
        session_attributes['riddle'] = active_scenario.riddle.id
        session_attributes['counter'] = active_scenario.state
        session_attributes['score'] = active_scenario.score

        card = SimpleCard(
            'Willkommen zurück',
            f'Das Spiel {active_scenario.scenario.name} wird fortgesetzt.\n\n'
            f'Dein noch ungelöstes Rätsel lautet:\n'
            f'{active_scenario.riddle.task}'
        )

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        card
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

    scenario, speech_text = choose_scenario(
        slots.get("scenario").value,
        slots.get("players").value
    )

    riddle = scenario.riddles.all()[counter]

    session_attributes['scenario'] = scenario.id
    session_attributes['counter'] = counter
    session_attributes['riddle'] = riddle.id
    session_attributes['score'] = 0

    speech_text = f'{speech_text}.\n<p>Hier kommt deine erste Frage:</p> <p>{riddle.task}</p>'

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

    # slots
    answer = slots.get("answer").value if slots.get("answer").value else slots.get("number").value

    # attributes
    counter = session_attributes['counter']
    scenario = Scenario.objects.get(id=session_attributes['scenario'])
    riddle = scenario.riddles.get(id=session_attributes['riddle'])
    score = session_attributes['score']

    # TODO: Alle Antwortmöglichkeiten nach Alexa kopieren
    if answer in riddle.solution.lower().split(', '):
        correct = riddle.correct
        counter += 1
        score += riddle.points
        if counter == scenario.riddles.count():
            speech_text = (
                f"<p>Super, du hast alle Rätsel richtig beantwortet!</p>\n"
                f"<p>Du hast {score} von {scenario.possible_points} möglichen Punkten erreicht.</p>"
            )
            set_should_end_session = True

            # TODO: Ist die Frage ob das gelöscht werden soll oder lieber erhalten bleiben,
            #  ich würde leiber ein Flag setzen der anzeigt das es beendet wurde..
            user = handler_input.request_envelope.context.system.user.user_id
            ActiveScenario.objects.get(user=user).delete()
        else:
            next_riddle = scenario.riddles.all()[counter]
            speech_text = f'<p>{correct}</p>\n\n<p>Auf zum nächsten Rätsel:</p>\n<p>{next_riddle.task}</p>'
            session_attributes['riddle'] = next_riddle.id
    else:
        speech_text = f'<p>{riddle.incorrect}</p>'
        score += MINUS_POINTS

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


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes

    if not session_attributes.get('scenario'):
        speech_text = (
            f'<p>Wähle ein Szenario aus.</p>\n'
            f'<p>Es stehen: {" oder ".join(Scenario.objects.values_list("name", flat=True))} zur Auswahl.</p>'
        )
    else:
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
        session_attributes['score'] += MINUS_POINTS

        speech_text = f'<p>Hier kommt dein Hinweis:</p>\n<p>{riddle.hints}</p>'

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

    speech_text = (
        f'<say-as interpret-as="interjection">ade</say-as>,\n'
        f'<p>ich warte hier auf dich.</p>'
    )

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

    if not session_attributes.get('scenario'):
        speech_text = (
            f'<p>Wähle ein Szenario aus.</p>\n'
            f'<p>Es stehen: {" oder ".join(Scenario.objects.values_list("name", flat=True))} zur Auswahl.</p>'
        )
    else:
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
        speech_text = f'<p>{riddle.incorrect}</p>'
        session_attributes['score'] += MINUS_POINTS

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

    logger.error(exception, exc_info=True)
    speech_text = f'<say-as interpret-as="interjection">ähm</say-as>, es gab wohl ein Problem!'

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response


skill = sb.create()
