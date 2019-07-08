from protocol import Protocol
import os

class KNX(Protocol): 
    """
        This is the class for Phillips Hue Stuff
    """
    
    def __init__(self, id, type): 
        pass

    def execute(self, id, value):
        #
        # This method execute the queries to the physical device
        #
        res = os.system("knxtool groupwrite ip:localhost {groupadress} {value}".format(groupadress=id, value=value))
        if res: 
            raise Exception("There was an error on KNX execution")