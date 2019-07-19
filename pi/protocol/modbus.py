import logging
from pymodbus.client.sync import ModbusTcpClient
import ast
import configparser

from .protocol import Protocol

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

config = configparser.ConfigParser()
f = config.read("conf/modbus.conf")
BOX_IP = config['DEFAULT']['IP_ADDRESS']

class Modbus(Protocol):
    """
    This is Modbus Master protocol.
    Example for device addresses:
        - Motor: 1
        - Magnet: 2
    """

    @staticmethod
    def execute(device, action):
        Modbus.send(device, eval(action['parameters']))

    @staticmethod
    def send(device, value):
        """
        This function writes a new value to a device of the given ip address.
        The value has to be a boolean. For example: True, to open the box by the motor (False -> close the box).
        """
        logger.debug('send method with device: {device} and value = {value}'.format(device=str(device), value=str(value)))

        try:
            client = ModbusTcpClient(BOX_IP, port=502, timeout=10)
            client.write_coil(device, value['value'])
            result = client.read_coils(device, 1)
            logger.debug(result)
            client.close()
        except RuntimeError as err:
            logger.debug(err)

    @staticmethod
    def read(ip_address, device_address):
        """
        This function reads the state of a device at the given address.
        For example: True, if the box is opened (False -> if the box is closed).
        """
        try:
            client = ModbusTcpClient(ip_address, port=502, timeout=10)
            result = client.read_coils(device_address, 1)
            logger.debug(result)
            client.close()
            return result.bits[0]
        except RuntimeError as err:
            logger.debug(err)
