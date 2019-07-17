from phue import Bridge
from rgbxy import Converter
from time import sleep
import ast
from .protocol import Protocol

WHITE = 'ffffff'
RED = 'ff0000'
# TODO: Kann sich immer wieder ändern, in Config schreiben?
IP_ADDRESS = '192.168.178.67'


class PHue(Protocol):
    """
        This is the class for Phillips Hue Stuff
    """

    # TODO: Error: Signature of method 'PHue.execute()' does not match signature of base method in class 'Protocol'
    @staticmethod
    def execute(device, action):
        #
        # This method execute the queries to the physical device
        #
        print(device, action)
        try:
            fun = getattr(PHue, action['function'])
            # TODO: func(device, **eval(action.parameters)), parameter in funktionen ausschreiben..
            fun(device, ast.literal_eval(action['parameters']))
        except Exception:
            print("execute without function")
            # TODO: Wann tritt dieser Fall auf?
            PHue.send(ast.literal_eval(action['parameters']), address=device)

    def send(*address, **value):
        print(address, value)
        b = Bridge(IP_ADDRESS)
        b.set_light(
            address,
            value
        )

    def turn_on(device, parameter):
        PHue.set_color(device, WHITE)

    def turn_off(device, parameter):
        value = {
            'transitiontime': 1,
            'on': False,
        }
        PHue.send(device, value)

    # TODO: alarm(self, tr_time, blink_count, hex_color=RED) --> Parameter auschreiben?
    def alarm(device, parameter):
        hex_color = parameter['hex_color'] if 'hex_color' in parameter else RED
        anim_in = {
            'transitiontime': parameter['tr_time'],
            'on': True,
            'bri': 254,
            'sat': 254,
            'xy': list(Converter().hex_to_xy(hex_color))
        }
        anim_out = {
            'transitiontime': parameter['tr_time'],
            'on': True,
            'bri': 5,
            'sat': 70,
            'xy': list(Converter().hex_to_xy(hex_color))

        }

        # TODO: muss verwendet werden.. statt parameter['sleep_time'] unten
        sleep_time = float(parameter['tr_time'] + 1) / 10.0

        for i in range(0, parameter['blink_count']):
            PHue.set_color(device, anim_in)
            sleep(parameter['sleep_time'])
            PHue.set_color(device, anim_out)
            sleep(parameter['sleep_time'])

    # TODO: Error: Usually first parameter of a method is named 'self'
    def set_color(device, parameter):
        value = {
            'transitiontime': 1,
            'on': True,
            'bri': 254,
            'sat': 254,
            'xy': list(Converter().hex_to_xy(parameter['hex_value']))
        }
        PHue.send(device, value)

    # TODO: Error: Signature of method 'PHue.wait()' does not match signature of base method in class 'Protocol'
    def wait(device, parameters):
        wait_time = parameters['sleep_time']
        sleep(wait_time)

    # TODO: alle Methoden sollten ein self haben..
    def connect(self):
        b = Bridge(IP_ADDRESS)

        # nur einmal, zu Hue Bridge connecten
        b.connect()
