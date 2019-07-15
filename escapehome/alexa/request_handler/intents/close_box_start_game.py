from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template
from core.models import Scenario
from alexa.request_handler.buildin.fallback import fallback_request


def close_box_start_game_request(handler_input, minus_points):
    """Handler to close box and start the game"""
    session_attributes = handler_input.attributes_manager.session_attributes

    # falls scenario noch nicht ausgewählt ist oder riddle bereits gestartet wurde
    if not session_attributes.get('scenario') or (
            session_attributes.get('scenario') and session_attributes.get('riddle')):
        return fallback_request(handler_input, minus_points)
    else:
        # TODO ist box wirklich geschlossen?
        # if box_open:
        #    card = "Schließe Box"
        # else:

        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        session_attributes['counter'] = 0
        session_attributes['riddle'] = scenario.riddles.first().id
        session_attributes['score'] = 0

        speech_text = get_template('skill/first_riddle.html').render(
            {'scenario': scenario, 'riddle': scenario.riddles.first()}
        )
        card = f'1. Rästel für Szenario: {scenario.name}'

        return handler_input.response_builder.speak(
            speech_text
        ).set_card(
            SimpleCard(
                card,
                BeautifulSoup(speech_text, features="html.parser").text
            )
        ).set_should_end_session(
            False
        ).response
