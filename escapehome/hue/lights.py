import time

from phue import Bridge, Light as HueLight

# IP Adresse der Hue Bridge rausfinden:
# https://www.meethue.com/api/nupnp
from rgbxy import Converter

IP_ADDRESS = '192.168.178.67'


class Hue:

    def __init__(self):
        self.bridge = Bridge(IP_ADDRESS)


class Light(Hue):

    def __init__(self, lamp_id):
        super().__init__()
        self.light = HueLight(self.bridge, lamp_id)

    def turn_on(self):
        # an
        self.light.on = True

    def turn_off(self):
        # aus
        self.light.on = False

    def set_saturation(self, value: int):
        # sättigung (schwach: 0 - stark: 254)
        self.light.saturation = value

    def set_brightness(self, value: int):
        # helligkeit (dunkel: 0 - hell: 254)
        self.light.brightness = value

    def set_color(self, hex_value=None):
        c = Converter()
        x, y = c.hex_to_xy(hex_value) if hex_value else c.get_random_xy_color()
        self.light.xy = [x, y]

    def blink(self, tr_time, blink_count):
        sleep_time = float(tr_time + 1) / 10.0

        for i in range(0, blink_count * 2):
            state = {
                'transitiontime': tr_time,
                'on': not self.light.on,
                'bri': self.light.brightness,
                'sat': self.light.saturation,
                'hue': self.light.hue
            }

            self.bridge.set_light(self.light.light_id, state)
            time.sleep(sleep_time)

    def alarm(self, tr_time, blink_count):
        anim_in = {
            'transitiontime': tr_time,
            'on': True,
            'bri': 254,
            # 'bri': self.light.brightness,
            'sat': 254,
            # 'sat': self.light.saturation,
            'hue': self.light.hue
        }
        anim_out = {
            'transitiontime': tr_time,
            'on': True,
            'bri': 5,
            'sat': 70,
            'hue': self.light.hue
        }

        sleep_time = float(tr_time + 1) / 10.0

        for i in range(0, blink_count):
            self.bridge.set_light(self.light.light_id, anim_in)
            time.sleep(sleep_time)
            self.bridge.set_light(self.light.light_id, anim_out)
            time.sleep(sleep_time)
