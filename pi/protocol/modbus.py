import logging
from pymodbus.client.sync import ModbusTcpClient
import ast

from .protocol import Protocol

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class Modbus(Protocol):
    """
    This is Modbus Master protocol.
    Example for device addresses:
        - Motor: 1
        - Magnet: 2
    """

    # TODO: Signature of method 'Modbus.execute()' does not match signature of base method in class 'Protocol'
    @staticmethod
    def execute(device, action):
        try:
            fun = getattr(Modbus, action['function'])
            fun(action['parameters'])
        except Exception:
            Modbus.send(device, value=action)

    # TODO: Signature of method 'Modbus.execute()' does not match signature of base method in class 'Protocol'
    @staticmethod
    def send(*address, **value):
        """
        This function writes a new value to a device of the given ip address.
        The value has to be a boolean. For example: True, to open the box by the motor (False -> close the box).
        """
        # print(value,' | ', address)
        try:
            ip_address = address[0]
            device_address = 1  # address['device_address']
            client = ModbusTcpClient(ip_address, port=502, timeout=10)
            v = ast.literal_eval(value['value']['parameters'])['value']
            client.write_coil(device_address, v)
            result = client.read_coils(device_address, 1)
            log.debug(result)
            client.close()
        except RuntimeError as err:
            log.debug(err)

    @staticmethod
    def read(ip_address, device_address):
        """
        This function reads the state of a device at the given address.
        For example: True, if the box is opened (False -> if the box is closed).
        """
        try:
            client = ModbusTcpClient(ip_address, port=502, timeout=10)
            result = client.read_coils(device_address, 1)
            log.debug(result)
            client.close()
            return result.bits[0]
        except RuntimeError as err:
            log.debug(err)
