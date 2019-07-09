import requests 
from time import sleep
import os
import json
import threading

API_URL = "https://homeescape.pythonanywhere.com/api/ready/"

devices = {}
execute_thread = None
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
        devices[j['id']] = j

def execute_steps(args): 
    """
        execute the json input from Server

        {
            meta{
                step_duration: 1, #duration between steps in secconds
                loop: 0, # repeat mode (0 = infinity or number of loops)
                loop_break_duration: 1, # duration between last step and restart at first step
                                # at loop
                    }
            steps{
                step{
                    position: 1, # to make a order of steps
                    function: “function_name”,
        values: {
        ‘brightness’: 100,
        } #value for step
        stop: “”  
                }
            }
        }
    """
    print(args)

def check_server(wait_time=0.5): 
    """
        send a request to django and check what he has to do 
    """
    res = requests.post(API_URL,json={"text":"was gibt es neues?" })
    
    if res.json(): 
        # stop currcent thread
        global execute_thread
        if execute_thread: 
            execute_thread.join()
        # execute steps in thread
        th = threading.Thread(target=execute_steps, args=(res.json()))
        th.start()
        execute_thread = th
    sleep(wait_time)

if __name__ == "__main__":
    while True: 
        check_server(wait_time=5)

