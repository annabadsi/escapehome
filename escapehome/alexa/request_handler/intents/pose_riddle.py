import datetime

from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from alexa.request_handler.buildin.cancel_and_stop import cancel_and_stop_request
from alexa.request_handler.buildin.fallback import fallback_request
from api.views import riddle_commands_to_json, box_command_to_json
from core.models import Scenario, ActiveScenario, Command


def pose_riddle_request(handler_input, minus_points, quit_minus_points):
    """Handler for Pose Riddle Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)

    # if box was opened in game
    if not session_attributes.get('box') and active_scenario.box:
        return cancel_and_stop_request(handler_input, quit_minus_points)

    if session_attributes.get('scenario') and not session_attributes.get('box'):
        slots = handler_input.request_envelope.request.intent.slots
        set_should_end_session = False
        next_riddle = None
        duration = None

        # slots
        answer = slots.get("answer").value if slots.get("answer").value else slots.get("number").value

        # attributes
        counter = session_attributes['counter']
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes['riddle'])
        score = session_attributes['score']

        if answer in riddle.solution.lower().split(', '):
            # Reset hint counter if answer correct
            session_attributes['hint_counter'] = 0
            # Set next Riddle
            counter += 1
            # Add points to the score
            score += riddle.points

            if counter == scenario.riddles.count():
                # Won: all puzzles answered
                set_should_end_session = True

                user = handler_input.request_envelope.context.system.user.user_id
                box_command_to_json(Command.objects.get(name='modbus box öffnen'), user)

                start_time = datetime.datetime.strptime(session_attributes.get('start_time'), '%Y-%m-%d %H:%M:%S.%f')
                now = datetime.datetime.now()

                duration = (active_scenario.duration + (now - start_time)).seconds / 60

                active_scenario.delete()
            else:
                # Gehe zum nächsten Rätsel
                next_riddle = scenario.riddles.order_by('orderedriddle')[counter]
                riddle_commands_to_json(next_riddle, user)

                session_attributes['riddle'] = next_riddle.id
        else:
            # Wrong answer
            score += minus_points

        speech_text = get_template('skill/riddle.html').render(
            {
                'score': score,
                'counter': counter,
                'scenario': scenario,
                'riddle': riddle,
                'next_riddle': next_riddle,
                'duration': duration,
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
                BeautifulSoup(speech_text, features="html.parser").text
            )
        ).set_should_end_session(
            set_should_end_session
        ).response
    else:
        return fallback_request(handler_input, minus_points, quit_minus_points)
