import requests
from time import sleep
import os
import json
import threading
import protocol as p
import ast

API_URL = "https://homeescape.pythonanywhere.com/api/commands/"
API_RESPONSE_URL = "https://homeescape.pythonanywhere.com/api/cancel/"

devices = {}
execute_threads = []
wait_time = 0.5
last_response = None


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

def execute_actions(protocol,device, actions): 
    for action in actions: 
        protocol.execute(device, action)

def execute_commands(*args):
    """
    execute the json input from Server

    args is a list of commands 
    """
    for command in args: 
        devices = ast.literal_eval(command['device'])
        for device in devices: 
            print(device)
            # execute steps for each device
            th = threading.Thread(target=execute_actions, args=(get_protocol(command['protocol']),device, command['actions']))
            execute_threads.append(th)
            th.start()
    


def check_server(wait_time=0.5):
    """
    send a request to django and check what he has to do
    """
    global execute_threads
    global last_response
    
    res = requests.post(API_URL, json={"text": "was gibt es neues?"})
    if res.text == last_response: 
        sleep(wait_time)
        return

    data = json.loads(res.text)
    if data:
        try:
            # stop currcent thread
            if execute_threads:
                for execute_thread in execute_threads:
                    execute_thread.join()
            # execute steps in thread
            if data['meta']['loop'] == 0:
                th = threading.Thread(target=execute_commands, args=(data['commands']))
                execute_threads.append(th)
                th.start()
            else: 
                for _ in range(data['meta']['loop']): 
                    execute_commands(data['commands'])
            
        except Exception as e: 
            print("Error in json")
            print(e)
    else: 
        # stop currcent thread 
        if execute_threads:
            for execute_thread in execute_threads:
                execute_thread.join()
    sleep(wait_time)

def check_box(wait_time=5): 
    """
    Check the Box if the user opens it
    """
    ip_address, device_address = ('123.2.1.2', '1')
    if p.Modbus.read(ip_address, device_address): 
        res = requests.post(API_RESPONSE_URL, json={"exit_game": True})
        exit(0)

if __name__ == "__main__":
    # inital the protocols
    c_th = threading.Thread(target=check_box, args=())
    while True:
        check_server(wait_time=5)
