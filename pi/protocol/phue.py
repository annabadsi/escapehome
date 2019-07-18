from phue import Bridge
from rgbxy import Converter
from time import sleep
from .protocol import Protocol

WHITE = 'ffffff'
RED = 'ff0000'
# TODO: in conf > hue.conf schreiben!
IP_ADDRESS = '192.168.43.155'


class PHue(Protocol):
    """
    This is the class for Phillips Hue Stuff
    """

    @staticmethod
    def execute(device, action):
        # This method execute the queries to the physical device
        try:
            fun = getattr(PHue, action['function'])
            fun(device, **eval(action['parameters']))
        except Exception as e:
            print("execute without function")
            PHue.send(device, *eval(action['parameters']))

    @staticmethod
    def send(address, value):
        print(address, value)
        b = Bridge(IP_ADDRESS)
        b.set_light(
            address,
            value
        )

    @staticmethod
    def turn_on(device):
        print('turn on ')
        PHue.set_color(device, WHITE)

    @staticmethod
    def turn_off(device):
        print('turn off')
        value = {
            'transitiontime': 1,
            'on': False
        }
        PHue.send(device, value)

    @staticmethod
    def alarm(device, tr_time, blink_count, hex_color=RED):
        anim_in = {
            'transitiontime': tr_time,
            'on': True,
            'bri': 254,
            'sat': 254,
            'xy': list(Converter().hex_to_xy(hex_color))
        }
        anim_out = {
            'transitiontime': tr_time,
            'on': True,
            'bri': 5,
            'sat': 70,
            'xy': list(Converter().hex_to_xy(hex_color))

        }

        sleep_time = float(tr_time + 1) / 10.0

        for i in range(0, blink_count):
            PHue.send(device, anim_in)
            sleep(sleep_time)
            PHue.send(device, anim_out)
            sleep(sleep_time)

    @staticmethod
    def wait(device, sleep_time):
        sleep(sleep_time)

    @staticmethod
    def set_color(device, hex_value):
        value = {
            'transitiontime': 1,
            'on': True,
            'bri': 254,
            'sat': 254,
            'xy': list(Converter().hex_to_xy(hex_value))
        }
        PHue.send(device, value)

    # TODO: rausnehmen? b returnen?
    @staticmethod
    def connect():
        b = Bridge(IP_ADDRESS)
