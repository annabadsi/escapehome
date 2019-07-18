import os
import ast

from .protocol import Protocol


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
            fun = getattr(KNX, action['function'])
            fun(action['parameters'])
        except Exception:
            print("execute without function")
            # TODO: **eval(action['parameters'])
            KNX.send(
                ast.literal_eval(action['parameters'])['value'],
                address=device
            )
        # KNX.execute(value, address)

    @staticmethod
    def send(*value, **address):
        print(f"knxtool groupswrite ip:localhost {address['address']} {value[0]}")
        res = os.system(
            "knxtool groupswrite ip:localhost {address} {value}".format(address=address['address'], value=value[0])
        )
        if res:
            raise Exception("There was an error on KNX execution")
