import requests
from time import sleep
import os
import json
import threading
import protocol as p
import ast

API_URL = "https://homeescape.pythonanywhere.com/api/commands/"

devices = {}
execute_threads = []
wait_time = 0.5


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
    res = requests.post(API_URL, json={"text": "was gibt es neues?"})
    
    data = json.loads(res.text)
    if data:
        try:
            # stop currcent thread
            global execute_threads
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
    sleep(wait_time)


if __name__ == "__main__":
    # inital the protocols
    while True:
        check_server(wait_time=5)
