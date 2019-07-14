from phue import Bridge, Light as HueLight
from rgbxy import Converter
from time import sleep
import ast
from .protocol import Protocol

WHITE = 'ffffff'
RED = 'ff0000'
IP_ADDRESS = '192.168.178.67'

class PHue(Protocol):
    """
        This is the class for Phillips Hue Stuff
    """

    @staticmethod
    def execute(device, action):
        #
        # This method execute the queries to the physical device
        #
        print(device, action)
        try:
            fun = getattr(PHue, action['function'])
            fun(device, ast.literal_eval(action['parameters']))
        except Exception: 
            print("execute without function")
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
    
    
    def alarm(device,parameter):
        hex_color = parameter['hex_color'] if 'hex_color' in parameter else RED
        anim_in = {
            'transitiontime': parameter['tr_time'],
            'on': True,
            'bri': 254,
            # 'bri': self.light.brightness,
            'sat': 254,
            # 'sat': self.light.saturation,
            'xy': list(Converter().hex_to_xy(hex_color))
        }
        anim_out = {
            'transitiontime': parameter['tr_time'],
            'on': True,
            'bri': 5,
            'sat': 70,
            'xy': list(Converter().hex_to_xy(hex_color))

        }

        sleep_time = float(parameter['tr_time'] + 1) / 10.0

        for i in range(0, parameter['blink_count']):
            PHue.set_color(device, anim_in)
            sleep(parameter['sleep_time'])
            PHue.set_color(device, anim_out)
            sleep(parameter['sleep_time'])

    def set_color(device, parameter):
        value = {
                'transitiontime': 1,
                'on': True,
                'bri': 254,
                'sat': 254,
                'xy': list(Converter().hex_to_xy(parameter['hex_value']))
                }
        PHue.send(device, value)
    
    def wait(device, parameters):
        wait_time = parameters['sleep_time']
        sleep(wait_time)

    def connect(self):
        b = Bridge(IP_ADDRESS)

        # nur einmal, zu Hue Bridge connecten
        b.connect()
