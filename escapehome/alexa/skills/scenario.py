from core.models import Scenario, ActiveScenario


def choose_scenario(name, players):
    scenarios = Scenario.objects.filter(name__contains=name)

    if scenarios:
        active_scenario = ActiveScenario.objects.create(scenario=scenarios[0], players=players)
        return f'<p>Um folgendes wird es gehen:</p> {active_scenario.scenario.description}'
    else:
        return f'<p>ich habe kein Szenario mit diesem Namen gefunden!</p>'
