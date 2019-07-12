#!/usr/bin/env python

from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from twisted.internet.task import LoopingCall
import RPi.GPIO as GPIO
import logging
import time
import os

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

MOTOR_PIN = 18
MAGNET_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(MAGNET_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
motor_opened = True


def move_motor(state):
    os.system('gpio -g mode {} pwm'.format(MOTOR_PIN))
    os.system('gpio pwm-ms')
    os.system('gpio pwmc 192')
    os.system('gpio pwmr 2000')
    if state:
        log.debug("Box auf")
        os.system('gpio -g pwm {} 60'.format(MOTOR_PIN))
        time.sleep(1)
    else:
        log.debug("Box zu")
        os.system('gpio -g pwm {} 145'.format(MOTOR_PIN))
        time.sleep(1)
    os.system('gpio -g mode 18 input')


def update_context(a):
    # check motor update
    global motor_opened
    context = a[0]
    register = 1
    slave_id = 0x00
    address = 0x01
    values = context[slave_id].getValues(register, address, count=1)
    if values[0] != motor_opened:
        motor_opened = values[0]
        move_motor(motor_opened)
    # update magnet in context
    address = 0x02
    values = [GPIO.input(MAGNET_PIN)]
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

    loop = LoopingCall(f=update_context, a=(context,))
    loop.start(0.5, now=False)
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))


if __name__ == "__main__":
    try:
        run_updating_server()
    except KeyboardInterrupt:
        print("Terminating")
    finally:
        GPIO.cleanup()
