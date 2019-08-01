import datetime
import os

from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from core.models import Scenario, ActiveScenario
from escapehome import settings


def launch_request(handler_input):
    """Handler for Skill Launch."""
    file_path = f"{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json"
    if os.path.exists(file_path):
        os.remove(file_path)

    session_attributes = handler_input.attributes_manager.session_attributes

    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario, created = ActiveScenario.objects.get_or_create(user=user)

    session_attributes['box'] = True
    session_attributes['start_time'] = datetime.datetime.strftime(
        handler_input.request_envelope.request.timestamp,
        '%Y-%m-%d %H:%M:%S.%f'
    )

    # new game
    if created or not active_scenario.scenario:
        speech_text = get_template('skill/welcome.html').render(
            {'scenarios': Scenario.objects.all()}
        )

    # continue game
    else:
        session_attributes['scenario'] = active_scenario.scenario.id
        session_attributes['riddle'] = active_scenario.riddle.id
        session_attributes['counter'] = active_scenario.state
        session_attributes['score'] = active_scenario.score

        speech_text = get_template('skill/welcome_back.html').render(
            {'active_scenario': active_scenario}
        )

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            f'Willkommen zu Escape Home',
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        False
    ).response
