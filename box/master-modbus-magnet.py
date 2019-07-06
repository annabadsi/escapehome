import RPi.GPIO as GPIO
from pymodbus.client.sync import ModbusTcpClient
import logging
import time

PIN = 15
IP_ADDRESS = '192.168.137.151'

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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    try:
        state = GPIO.input(PIN)
        while True:
            new_state = GPIO.input(PIN)
            if new_state != state:
	        state = new_state
	        if state == 1:
                    write_via_tcp_modbus(True)
		    print "it's open!"
	        else:
                    write_via_tcp_modbus(False)
		    print "closed"
	    time.sleep(1)
    except KeyboardInterrupt:
        print(" Terminating..")
    finally:
        GPIO.cleanup()
