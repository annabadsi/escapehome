from core.models import Riddle
from hue.lights import Hue
from threading import Thread


h = Hue()

# Lampe an, warten, aus
for command in Riddle.objects.first().commands.all():
    for action in command.actions.all().order_by('orderedaction'):
        print(action)
        func = getattr(h, action.function)
        lights = command.devices.values_list('lamp__lamp_id', flat=True)
        h.lights = lights
        func(**eval(action.parameters))


# Lampe blinken
for command in Riddle.objects.last().commands.all():
    print(command)
    for action in command.actions.all().order_by('orderedaction'):
        func = getattr(h, action.function)
        lights = command.devices.values_list('lamp__lamp_id', flat=True)
        print(lights, action)
        h.lights = lights
        func(**eval(action.parameters))

