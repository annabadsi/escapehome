import datetime

from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from api.views import box_command_to_json
from core.models import Scenario, ActiveScenario, Command


def exception_request(handler_input, exception, logger):
    """Catch all exception handler, log exception and respond with custom message."""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id

    if not session_attributes.get('box'):
        # reopen box
        box_command_to_json(Command.objects.get(name='modbus box öffnen'), user)
        session_attributes['box'] = True

        # get scenario from session attributes
        scenario = Scenario.objects.filter(id=session_attributes.get('scenario', None)).first()

        # get playing time
        duration = 0
        if session_attributes.get('start_time'):
            start_time = datetime.datetime.strptime(session_attributes.get('start_time'), '%Y-%m-%d %H:%M:%S.%f')
            now = datetime.datetime.now()
            duration = now - start_time

        # save attributes in database
        active_scenario = ActiveScenario.objects.get(user=user)
        active_scenario.scenario = scenario
        active_scenario.riddle = scenario.riddles.filter(id=session_attributes.get('riddle', None)).first()
        active_scenario.players = session_attributes.get('players', 0)
        active_scenario.state = session_attributes.get('counter', 0)
        active_scenario.score = session_attributes.get('score', 0)
        active_scenario.duration = session_attributes.get('duration', 0) + duration
        active_scenario.save()

    logger.error(exception, exc_info=True)

    speech_text = get_template('skill/exception.html').render()

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Oops, ...",
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).set_should_end_session(
        True
    ).response
