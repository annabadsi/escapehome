from protocol import Protocol
from phue import Bridge

class PHue(Protocol): 
    """
        This is the class for Phillips Hue Stuff
    """
    
    def __init__(self, id, type): 
        self.IP_ADDRESS = '192.168.178.67'
    @classmethod
    def execute(cls, args):
        #
        # This method execute the queries to the physical device
        #
        pass

    def connect(self): 
        b = Bridge(self.IP_ADDRESS)

        # nur einmal, zu Hue Bridge connecten
        b.connect()
    