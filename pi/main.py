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

    This function is not used yet but the Idea is to send the possible Devices to the Webserver to make
    configurations easy.

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
    """
    Look up for a given Protocol define at the Protocol Package.
    String => Class
    :param protocol:
    :return:
    """
    return getattr(p, protocol)


def execute_actions(protocol, device, actions):
    """
    iterate through the actions and call the execute method at the Protocol class
    :param protocol:
    :param device:
    :param actions:
    :return:
    """
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
            # Kill the Thread from outer scope
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
    """
    get the data from the server
    if no connection can be set the return is None
    :return:
    """
    try:
        res = requests.post(API_URL, timeout=5)
        result = res.text
        logger.debug(result)
        res.connection.close()
    except Exception as e:
        logger.error(e)
        result = None
    return result


def ping_file():
    """
    Test function for Debugging without Server
    ! DO NOT USE IN PRODUCTION ! (Because it won't work)
    :return:
    """
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
            # only for debug issiue
            response = ping_file()
        if response == last_response:
            # The response is already processed
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
                    KILL_FLAG = True  # soft kill :D
                    execute_thread.join()
                    KILL_FLAG = False

                if command_threads:
                    for cth in command_threads:
                        cth.join()
                    command_threads = []
                if not user_id:
                    user_id = data['meta']['user_id'] # userID given from alexa to identify the player
                # execute steps in thread
                execute_thread = Thread(
                    target=execute_commands,
                    args=(data['meta']['loop'], data['commands'])
                )
                logger.debug(execute_thread)
                execute_thread.start()

            except Exception as e:
                logger.error("Error at json parser")
                logger.error(e)
        else:
            # stop currcent thread
            if execute_thread:
                execute_thread.join()

            if command_threads:
                for cth in command_threads:
                    cth.join()
                command_threads = []
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

    # Thread for check data from Server
    check_server_thread = Thread(
        target=check_server,
        args=()
    )

    # Thread for check if Box was open
    check_box_thread = Thread(
        target=check_box,
        args=()
    )

    check_server_thread.start()
    check_box_thread.start()

    while check_server_thread:
        # do not terminate System while check server thread is processing
        pass

