from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from api.views import box_command_to_json
from core.models import Scenario, ActiveScenario, Command
from alexa.request_handler.buildin.fallback import fallback_request


def close_box_start_game_request(handler_input, minus_points, quit_minus_points):
    """Handler to close box and start the game"""
    session_attributes = handler_input.attributes_manager.session_attributes

    # scenario selected and box still opened
    if session_attributes.get('scenario') and session_attributes.get('box'):
        user = handler_input.request_envelope.context.system.user.user_id
        active_scenario = ActiveScenario.objects.get(user=user)

        # check if box is closed at all
        if active_scenario.box:
            speech_text = get_template('skill/close_box.html').render()
            return handler_input.response_builder.speak(
                speech_text
            ).set_card(
                SimpleCard(
                    "Schließe auch die hintere Tür der Box.",
                    BeautifulSoup(speech_text, features="html.parser").text
                )
            ).set_should_end_session(
                False
            ).response
        else:
            box_command_to_json(Command.objects.get(name='modbus box schließen'), user)
            session_attributes['box'] = False
            scenario = Scenario.objects.get(id=session_attributes['scenario'])

            # new game will be started
            if not session_attributes.get('riddle'):
                riddle = scenario.riddles.order_by('orderedriddle').first()
                counter = 0
                session_attributes['score'] = 0
                session_attributes['counter'] = counter
                session_attributes['riddle'] = riddle.id

                speech_text = get_template('skill/first_riddle.html').render(
                    {'scenario': scenario, 'riddle': riddle}
                )
            # game will be continued
            else:
                counter = session_attributes['counter']
                riddle = scenario.riddles.get(id=session_attributes['riddle'])

                speech_text = get_template('skill/first_riddle.html').render(
                    {'scenario': None, 'riddle': riddle}
                )

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
    else:
        return fallback_request(handler_input, minus_points, quit_minus_points)
