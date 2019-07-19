from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from alexa.request_handler.buildin.cancel_and_stop import cancel_and_stop_request
from core.models import Scenario, ActiveScenario


def help_request(handler_input, minus_points, quit_minus_points):
    """Handler for Help Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)
    hint = None

    # if box was opened in game
    if not session_attributes.get('box') and active_scenario.box:
        return cancel_and_stop_request(handler_input, quit_minus_points)

    if session_attributes.get('scenario') and not session_attributes.get('box'):
        scenario = Scenario.objects.get(id=session_attributes.get('scenario', None))
        riddle = scenario.riddles.get(id=session_attributes.get('riddle', None))

        # set und get hint counter
        counter = session_attributes.get('hint_counter', 0)
        session_attributes['hint_counter'] = counter + 1

        hints = riddle.hints.split('|')
        # if all notes run through, always use the last one.
        if hints:
            hint = hints[counter].strip() if len(hints) > counter else hints[-1]
            session_attributes['score'] += minus_points

        header = 'Hinweis'
        speech_text = get_template('skill/hint.html').render({'hint': hint})
    elif session_attributes.get('scenario'):
        header = 'Spiel Vorbereitungen'
        speech_text = get_template('skill/close_box.html').render()
    else:
        header = 'Szeanrio Auswahl'
        speech_text = get_template('skill/choose_scenario.html').render(
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
            header,
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).response
