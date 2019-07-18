import time

from phue import Bridge, Light as HueLight

# IP Adresse der Hue Bridge rausfinden:
# https://www.meethue.com/api/nupnp
from rgbxy import Converter

# IP_ADDRESS = '10.27.99.18'
# IP_ADDRESS = '192.168.178.88'
IP_ADDRESS = '172.20.10.7'
WHITE = 'ffffff'
RED = 'ff0000'


class Hue:

    def __init__(self):
        self.bridge = Bridge(IP_ADDRESS)
        self.lights = None

    def turn_on(self):
        self.set_color(WHITE)

    def turn_off(self):
        self.bridge.set_light(
            self.lights,
            {
                'transitiontime': 1,
                'on': False,
            }
        )

    def set_color(self, hex_value):
        self.bridge.set_light(
            self.lights,
            {
                'transitiontime': 1,
                'on': True,
                'bri': 254,
                'sat': 254,
                'xy': list(Converter().hex_to_xy(hex_value))
            }
        )

    def wait(self, sleep_time):
        time.sleep(sleep_time)

    def alarm(self, tr_time, blink_count, hex_color=RED):
        anim_in = {
            'transitiontime': tr_time,
            'on': True,
            'bri': 254,
            # 'bri': self.light.brightness,
            'sat': 254,
            # 'sat': self.light.saturation,
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
            self.bridge.set_light(self.lights, anim_in)
            time.sleep(sleep_time)
            self.bridge.set_light(self.lights, anim_out)
            time.sleep(sleep_time)

    def blink(self, tr_time, blink_count, hex_color=WHITE):
        sleep_time = float(tr_time + 1) / 10.0

        for i in range(0, blink_count):
            state_on = {
                'transitiontime': tr_time,
                'on': True,
                'bri': 254,
                'sat': 254,
                'xy': list(Converter().hex_to_xy(hex_color))
            }

            state_off = {
                'transitiontime': tr_time,
                'on': False,
            }

            self.bridge.set_light(self.lights, state_on)
            time.sleep(sleep_time)
            self.bridge.set_light(self.lights, state_off)
            time.sleep(sleep_time)

        self.turn_off()
