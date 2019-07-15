from ask_sdk_model.ui import SimpleCard
from bs4 import BeautifulSoup
from django.template.loader import get_template

from core.models import Scenario, ActiveScenario


def cancel_and_stop_request(handler_input):
    """Single handler for Cancel and Stop Intent."""
    session_attributes = handler_input.attributes_manager.session_attributes

    # TODO: nicht nur beim Beenden speichern sondern nach jedem Request? Falls bei Fehler nicht gespeicht wird
    # attributes
    scenario = Scenario.objects.get(id=session_attributes['scenario'])
    riddle = scenario.riddles.get(id=session_attributes['riddle'])
    score = session_attributes['score']
    counter = session_attributes['counter']

    # in model speichern
    user = handler_input.request_envelope.context.system.user.user_id
    active_scenario = ActiveScenario.objects.get(user=user)
    active_scenario.scenario = scenario
    active_scenario.riddle = riddle
    active_scenario.score = score
    active_scenario.state = counter
    active_scenario.save()

    speech_text = get_template('skill/cancel_and_stop.html').render()

    return handler_input.response_builder.speak(
        speech_text
    ).set_card(
        SimpleCard(
            "Auf Wiedersehen",
            BeautifulSoup(speech_text, features="html.parser").text
        )
    ).response
