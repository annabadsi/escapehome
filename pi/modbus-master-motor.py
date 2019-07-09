from pymodbus.client.sync import ModbusTcpClient
import logging
import time

IP_ADDRESS = '192.168.137.72'
MOTOR_ADDRESS = 1
MAGNET_ADDRESS = 2

FORMAT = ('%(asctime)-15s %(threadName)-15s '
'%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def write_via_tcp_modbus(address, state):
    try:
        client = ModbusTcpClient(IP_ADDRESS, port=502, timeout=10)
        client.write_coil(address, state)
        result = client.read_coils(address, 1)
        log.debug(result)
        print result.bits[0]
        client.close()
    except RuntimeError as err:
        log.debug(err)

def read_via_tcp_modbus(address):
    try:
        client = ModbusTcpClient(IP_ADDRESS, port=502, timeout=10)
        result = client.read_discrete_inputs(address, 1)
        log.debug(result)
        print result.bits[0]
        client.close()
    except RuntimeError as err:
        log.debug(err)

if __name__ == '__main__':
    read_via_tcp_modbus(MAGNET_ADDRESS)
    #write_via_tcp_modbus(MOTOR_ADDRESS, True)
    #time.sleep(10)
    #write_via_tcp_modbus(MOTOR_ADDRESS, False)
