from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from alexa.request_handler.buildin.fallback import fallback_request
from core.models import Scenario, ActiveScenario


def pose_riddle_request(handler_input, minus_points):
    """Handler for Pose Riddle Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes
    if not session_attributes.get('scenario'):
        return fallback_request(handler_input, minus_points)
    else:
        slots = handler_input.request_envelope.request.intent.slots
        set_should_end_session = False
        next_riddle = None

        # slots
        answer = slots.get("answer").value if slots.get("answer").value else slots.get("number").value

        # attributes
        counter = session_attributes['counter']
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes['riddle'])
        score = session_attributes['score']

        if answer in riddle.solution.lower().split(', '):
            # Richtige Antwort
            counter += 1
            score += riddle.points
            if counter == scenario.riddles.count():
                # Gewonnen: alle Rätsel beantwortet
                set_should_end_session = True

                # TODO: active sceanario in history speichern
                user = handler_input.request_envelope.context.system.user.user_id
                ActiveScenario.objects.get(user=user).delete()
            else:
                # Gehe zum nächsten Rätsel
                next_riddle = scenario.riddles.all()[counter]

                # TODO: Das übernimmt der PI dann
                if next_riddle.commands.all():
                    pass

                session_attributes['riddle'] = scenario.riddles.all()[counter].id
        else:
            # Falsche Antwort
            score += minus_points

        speech_text = get_template('skill/riddle.html').render(
            {
                'score': score,
                'counter': counter,
                'scenario': scenario,
                'riddle': riddle,
                'next_riddle': next_riddle,
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
                f'Deine Antwort für die Frage: {riddle.task} lautete "{answer}"\n\n.'
                f'{BeautifulSoup(speech_text, features="html.parser").text}'
            )
        ).set_should_end_session(
            set_should_end_session
        ).response
