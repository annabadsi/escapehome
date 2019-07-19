import os

from .protocol import Protocol

import logging

logger = logging.getLogger(__name__)


class KNX(Protocol):
    """
    This is the class for Phillips Hue Stuff
    """

    @staticmethod
    def execute(device, action):
        #
        # This method execute the queries to the physical device
        #
        # TODO: anpassen
        print(device, action)
        try:
            if not action['function']:
                action['function'] = ""
            fun = getattr(KNX, action['function'])
            print('parameter', action['parameters'], type(action['parameters']))
            print(fun)
            fun(**eval(action['parameters']))
        except Exception as e:
            print("execute without function")
            KNX.send(
                device,
                **eval(action['parameters'])
            )

    @staticmethod
    def send(address, value):
        print(type(value), value, type(address), address)
        if type(value) == list:
            value = value[0]
        command = "knxtool groupswrite ip:localhost {address} {value}".format(address=address, value=value)
        logger.debug('KNX command:', command)
        res = os.system(command)
        if res:
            logger.error('KNX Command return ', res)
            raise Exception("There was an error on KNX execution")
