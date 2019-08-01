import requests
from time import sleep
import os
import json
from threading import Thread
import protocol as p
import configparser
import logging

API_URL = "https://homeescape.pythonanywhere.com/api/commands/"
API_RESPONSE_URL = "https://homeescape.pythonanywhere.com/api/cancel/"
BOX_MOTOR_ID = None

devices = {}
execute_thread = None
command_threads = []

wait_time = 1
last_response = None
user_id = None
logger = logging.getLogger(__name__)
KILL_FLAG = False


def update_devices():
    """
    update the devices dic and get new devices (if there are new)
    """
    devices = {}
    # open devices
    device_list = os.listdir("devices/")
    for dev in device_list:
        f = open("devices/" + dev)
        s = f.read()
        j = json.loads(s)
        if j['protocol'] not in devices:
            devices[j['protocol']] = {}
        devices[j['protocol']][j['id']] = j


def get_protocol(protocol):
    return getattr(p, protocol)


def execute_actions(protocol, device, actions):
    for action in actions:
        protocol.execute(device, action)


def execute_commands(loops, args):
    """
    execute the json input from Server

    args is a list of commands 
    """
    global KILL_FLAG
    for _ in range(loops):
        logger.debug('in the loop')
        if KILL_FLAG:
            logger.debug('KILLED')
            break
        for command in args:
            devices = command['devices']
            for device in devices:
                logger.debug(device)
                # execute steps for each device
                th = Thread(
                    target=execute_actions,
                    args=(
                        get_protocol(command['protocol']),
                        device,
                        command['actions']),
                )
                command_threads.append(th)
                th.start()
        for cth in command_threads:
            cth.join()


def ping_server():
    try:
        res = requests.post(API_URL, timeout=5)
        result = res.text
        logger.debug(result)
        res.connection.close()
    except Exception as e:
        print(e)
        result = None
    return result


# TODO: nur Test, noch rausnehmen
def ping_file():
    dat = open("test/test.json").read()
    return dat


def check_server(server=True):
    """
    send a request to django and check what he has to do
    """
    global execute_thread
    global command_threads
    global last_response
    global user_id
    global KILL_FLAG
    while True:
        if server:
            response = ping_server()
        else:
            response = ping_file()
        if response == last_response:
            logger.debug('i do nothing')
            continue
        if not response:
            logger.error('No response')
            continue

        last_response = response
        data = json.loads(response)
        logger.debug("data", data)
        if data:
            try:
                # stop currcent thread
                if execute_thread:
                    KILL_FLAG = True
                    execute_thread.join()
                    KILL_FLAG = False

                if command_threads:
                    for cth in command_threads:
                        cth.join()
                    command_threads = []
                if not user_id:
                    user_id = data['meta']['user_id']
                # execute steps in thread
                execute_thread = Thread(
                    target=execute_commands,
                    args=(data['meta']['loop'], data['commands'])
                )
                print('!!', execute_thread)
                execute_thread.start()
                print('&&', execute_thread)

            except Exception as e:
                print("Error in json")
                print(e)
        else:
            # stop currcent thread
            if execute_thread:
                execute_thread.join()

            if command_threads:
                for cth in command_threads:
                    cth.join()
                command_threads = []
    # TODO: unreachable code
    sleep(wait_time)


def check_box(sleep_time=2):
    """
    Check the Box if the user opens it
    If the status of the Box changed, the Server will be informed
    """
    global user_id
    prev_box_status = None

    while True:
        try:
            current_modbus_status = p.Modbus.read()
            if user_id and current_modbus_status != prev_box_status:
                # check if the user_id is set
                # only do something if the status of the box changed
                res = requests.post(API_RESPONSE_URL, json={"exit_game": bool(current_modbus_status), 'user': user_id})
                logger.debug(res.__dict__)
                prev_box_status = current_modbus_status
        except Exception as e:
            logger.error(e)
        sleep(sleep_time)


if __name__ == "__main__":
    # inital the protocols
    # c_th = threading.Thread(target=check_box, args=())

    # make configurations
    #config = configparser.ConfigParser()
    #if not BOX_IP or not BOX_MOTOR_ID:
    #    f = config.read("conf/modbus.conf")
    #    BOX_IP = config['DEFAULT']['IP_ADDRESS']
    #    BOX_MOTOR_ID = config['DEFAULT']['BOX_MOTOR_ID']

    wait_time = 5
    check_server_thread = Thread(
        target=check_server,
        args=()
    )
    check_box_thread = Thread(
        target=check_box,
        args=()
    )
    check_server_thread.start()
    check_box_thread.start()
    while check_server_thread:
        pass

    # while True:
    #   try:
    #       #check_box()
    #       check_server(False)
    #  except Exception as e:
    #      print(e)
