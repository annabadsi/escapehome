from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from alexa.request_handler.buildin.cancel_and_stop import cancel_and_stop_request
from core.models import Scenario, ActiveScenario


def fallback_request(handler_input, minus_points, quit_minus_points):
    """Fallback Handler"""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)

    # if box was opened in game
    if not session_attributes.get('box') and active_scenario.box:
        return cancel_and_stop_request(handler_input, quit_minus_points)

    # if false answer to riddle was given
    elif session_attributes.get('scenario') and not session_attributes.get('box'):
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
        session_attributes['score'] += minus_points
        header = 'Falsche Antwort'
        speech_text = get_template('skill/wrong_answer.html').render({'riddle': riddle})

    # if scenario is selected but box is still open
    elif session_attributes.get('scenario'):
        header = 'Spiel Vorbereitungen'
        speech_text = get_template('skill/close_box.html').render()

    # if scenario still isn't selected
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
