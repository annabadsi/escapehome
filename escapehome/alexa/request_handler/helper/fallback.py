from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from core.models import Scenario


def fallback_request(handler_input, minus_points):
    """Fallback Handler"""
    session_attributes = handler_input.attributes_manager.session_attributes
    riddle = None

    if session_attributes.get('scenario'):
        scenario = Scenario.objects.get(id=session_attributes['scenario'])
        riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
        session_attributes['score'] += minus_points

    speech_text = get_template('skill/fallback.html').render(
        {
            'scenario': session_attributes.get('scenario'),
            'scenarios': Scenario.objects.all(),
            'riddle': riddle,
        }
    )

    return handler_input.response_builder.speak(
            speech_text
        ).ask(
            speech_text
        ).set_card(
            SimpleCard(
                "Du brauchst Hilfe?",
                BeautifulSoup(speech_text, features="html.parser").text
            )
        ).response
