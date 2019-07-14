from phue import Bridge

from pi.protocol.protocol import Protocol


class PHue(Protocol):
    """
        This is the class for Phillips Hue Stuff
    """

    def __init__(self, protocol_id, protocol_type):
        super().__init__(protocol_id, protocol_type)
        self.IP_ADDRESS = '192.168.178.67'
        

    @classmethod
    def execute(cls, *value, **address):
        #
        # This method execute the queries to the physical device
        #
        pass

    def connect(self):
        b = Bridge(self.IP_ADDRESS)

        # nur einmal, zu Hue Bridge connecten
        b.connect()
