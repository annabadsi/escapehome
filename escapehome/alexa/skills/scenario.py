from core.models import Scenario


def choose_scenario(name):
    scenarios = Scenario.objects.filter(name__contains=name)
    speech = f'Gut, lass uns mit dem Szenario "{name}" loslegen.'

    if scenarios:
        scenario = scenarios[0]
        return speech + f'<p>Um folgendes wird es gehen:</p> {scenario.description}'
    else:
        return speech + f'<p>ich habe kein Szenario mit diesem Namen gefunden!</p>'

