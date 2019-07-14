import os

from pi.protocol.protocol import Protocol


class KNX(Protocol):
    """
        This is the class for Phillips Hue Stuff
    """

    @staticmethod
    def execute(*value, **address):
        #
        # This method execute the queries to the physical device
        #
        # TODO: anpassen
        res = os.system(f"knxtool groupwrite ip:localhost {address} {value}")
        if res:
            raise Exception("There was an error on KNX execution")
