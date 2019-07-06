from pymodbus.client.sync import ModbusTcpClient
import logging
import time

IP_ADDRESS = '192.168.137.72'

FORMAT = ('%(asctime)-15s %(threadName)-15s '
'%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def write_via_tcp_modbus(state):
    try:
        client = ModbusTcpClient(IP_ADDRESS, port=502, timeout=10)
        client.write_coil(1, state)
        result = client.read_coils(1, 1)
        print result.bits[0]
        client.close()
    except RuntimeError as err:
        log.debug(err)

if __name__ == '__main__':
    write_via_tcp_modbus(True)
    time.sleep(10)
    write_via_tcp_modbus(False)
