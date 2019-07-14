from django.template.loader import get_template

from core.models import Scenario, ActiveScenario


def exception_request(handler_input, exception, logger):
    """Catch all exception handler, log exception and respond with custom message."""
    session_attributes = handler_input.attributes_manager.session_attributes

    # TODO: nicht nur beim Beenden speichern sondern nach jedem Request? Falls bei Fehler nicht gespeicht wird
    # attributes
    scenario = Scenario.objects.get(id=session_attributes.get('scenario'))
    riddle = scenario.riddles.get(id=session_attributes.get('riddle'))
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

    logger.error(exception, exc_info=True)

    speech_text = get_template('skill/exception.html').render()

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response
