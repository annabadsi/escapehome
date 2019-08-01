import datetime
import os

from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from api.views import box_command_to_json
from core.models import Scenario, ActiveScenario, Command
from escapehome import settings


def cancel_and_stop_request(handler_input, quit_minus_points):
    """Single handler for Cancel and Stop Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    in_game = False

    if not session_attributes.get('box'):
        in_game = True

        # reopen box
        box_command_to_json(Command.objects.get(name='modbus box öffnen'), user)
        session_attributes['box'] = True

        # get scenario from session attributes
        scenario = Scenario.objects.filter(id=session_attributes.get('scenario', None)).first()

        # get playing time
        now = datetime.datetime.now()
        start_time = datetime.datetime.strptime(session_attributes.get('start_time', str(now)), '%Y-%m-%d %H:%M:%S.%f')

        # save attributes in database
        active_scenario = ActiveScenario.objects.get(user=user)
        active_scenario.scenario = scenario
        active_scenario.riddle = scenario.riddles.filter(id=session_attributes.get('riddle', None)).first()
        active_scenario.players = session_attributes.get('players', 0)
        active_scenario.state = session_attributes.get('counter', 0)
        active_scenario.score = session_attributes.get('score', 0) + quit_minus_points
        active_scenario.duration += (now - start_time)
        active_scenario.save()

    speech_text = get_template('skill/cancel_and_stop.html').render({'ingame': in_game})

    file_path = f"{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json"
    if os.path.exists(file_path):
        os.remove(file_path)

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Auf Wiedersehen",
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        True
    ).response
