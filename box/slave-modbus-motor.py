#!/usr/bin/env python

from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from twisted.internet.task import LoopingCall
import RPi.GPIO as GPIO
import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

SERVO_PIN = 12
MAGNET_PIN = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(MAGNET_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

servo = GPIO.PWM(SERVO_PIN, 50)
motor_opend = True
magnet_opend = False


def updating_motor(a):
    global motor_opend
    context = a[0]
    register = 1
    slave_id = 0x00
    address = 0x01
    values = context[slave_id].getValues(register, address, count=1)
    if values[0] != motor_opend:
        motor_opend = values[0]
        if motor_opend == True:
            log.debug("Drehung auf 0 Grad (box auf)")
            servo.ChangeDutyCycle(2.5)
        else:
            log.debug("Drehung auf 90 Grad (box zu)")
            servo.ChangeDutyCycle(7.5)


def updating_magnet_in_context(a):
    global magnet_opend
    new_value = GPIO.input(MAGNET_PIN)
    log.debug("check if box is opend or closed by magnet")
    if new_value != magnet_opend:
        log.debug("set magnet in context 0x02")
        context = a[0]
        register = 1
        slave_id = 0x00
        address = 0x02
        values = [new_value]
        context[slave_id].setValues(register, address, values)


def run_updating_server():
    # initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100))
    context = ModbusServerContext(slaves=store, single=True)

    # initialize the server information
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '2.2.0'

    motor_loop = LoopingCall(f=updating_motor, a=(context,))
    magnet_loop = LoopingCall(f=updating_magnet_in_context, a=(context,))
    motor_loop.start(0.5, now=False)
    magnet_loop.start(0.1, now=False)
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))


if __name__ == "__main__":
    try:
        servo.start(7.5)
        run_updating_server()
    except KeyboardInterrupt:
        print("Terminating")
    finally:
        servo.stop()
        GPIO.cleanup()
