import os
from time import sleep

from .protocol import Protocol

import logging

logger = logging.getLogger(__name__)


class KNX(Protocol):
    """
    This is the class for KNX

    Gruppenadressen zum Schalten der Deckenlampen:
        0/0/1 - Deckenlampe 1
        0/0/2 - Deckenlampe 2

        Gruppenadressen zum Fahren der Jalousien:
        3/1/1 - Jalousie 1 01 hoch // 00 runter
        3/1/2 - Jalousie 2 01 hoch // 00 runter
        3/1/3 - Jalousie 3 01 hoch // 00 runter

        Gruppenadressen zum Verstellen der Jalousien:
        3/2/1 - Jalousie 1
        3/2/2 - Jalousie 2
        3/2/3 - Jalousie 3

        Bei Fahren muss darauf geachtet werden, dass die Jalousien erst kurz verstellt werden muessen bevor sie fahren
        koennen
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
            fun(device, **eval(action['parameters']))
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


    @staticmethod
    def jalousie_reset(device):
        KNX.send(device, 0)
        sleep(65)


