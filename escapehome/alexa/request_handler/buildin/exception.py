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

        if session_attributes.get('scenario') and session_attributes.get('riddle') and session_attributes.get('score') and session_attributes.get('counter'):
            # get session attributes
            scenario = Scenario.objects.get(id=session_attributes['scenario'])
            riddle = scenario.riddles.get(id=session_attributes['riddle'])
            score = session_attributes['score']
            counter = session_attributes['counter']

            # save attributes in database
            active_scenario = ActiveScenario.objects.get(user=user)
            active_scenario.scenario = scenario
            active_scenario.riddle = riddle
            active_scenario.score = score
            active_scenario.state = counter
            active_scenario.save()
        else:
            print("Something went wrong in exception handling")

    logger.error(exception, exc_info=True)

    speech_text = get_template('skill/exception.html').render()

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response
