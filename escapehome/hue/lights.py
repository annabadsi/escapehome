import time

from phue import Bridge, Light as HueLight

# IP Adresse der Hue Bridge rausfinden:
# https://www.meethue.com/api/nupnp
from rgbxy import Converter

IP_ADDRESS = '10.27.99.18'
# IP_ADDRESS = '192.168.178.67'
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

    def blink(self, tr_time, blink_count):
        sleep_time = float(tr_time + 1) / 10.0
        self.turn_on()

        for light_id in self.lights:
            light = HueLight(self.bridge, light_id)
            for i in range(0, blink_count * 2):
                state = {
                    'transitiontime': tr_time,
                    'on': not light.on,
                    'bri': light.brightness,
                    'sat': light.saturation,
                    'hue': light.hue
                }

                self.bridge.set_light(light.light_id, state)
                time.sleep(sleep_time)

        self.turn_off()
