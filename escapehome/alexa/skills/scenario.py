from core.models import Scenario

# TODO: kann eigentlich weg
def choose_scenario(name, players):
    scenario = Scenario.objects.get(name__contains=name)

    if scenario:
        return (
            scenario,
            f'<p>Um folgendes wird es gehen:</p> {scenario.description}'
        )
    else:
        return (
            None,
            f'<p>ich habe kein Szenario mit diesem Namen gefunden!</p>'
        )
