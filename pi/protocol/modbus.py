import logging
from pymodbus.client.sync import ModbusTcpClient

from pi.protocol.protocol import Protocol

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

    @staticmethod
    def execute(value, *address):
        """
            This function writes a new value to a device of the given ip address.
            The value has to be a boolean. For example: True, to open the box by the motor (False -> close the box).
        """
        try:
            ip_address, device_address = address
            client = ModbusTcpClient(ip_address, port=502, timeout=10)
            client.write_coil(device_address, value)
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
