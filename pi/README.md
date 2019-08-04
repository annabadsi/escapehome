# EscapeHome (Pi Folder)
This is the Folder for the Pi where Escapehome is running
# Dependencies
To work with the different Protocols you need some Dependencies installed
### PHue
For the PHue you need nothing special 
### KNX
You have to install knxd on the raspberry pi. This takes a while !!!
https://sarwiki.informatik.hu-berlin.de/KNXD_Tutorial
### Modbus
TBD

# Quick start
1. Checkout the Project on the Raspberry Pi 
2. create a virtualenv with python3
3. activate the virtualenv with . venv/bin/activate
4. install requirements from the requirements.txt file 
5. execute main.py  

# Documentation

The whole Device System is based on Folder. In Devices are the definition
of devices (not used yet). To configurate the devices use the .conf files
in the conf folder. The Protocols are found at the protocol folder. 

The main.py is for the main connection to the pyhtonanywhere server and controlling of devices


##Protocols
###KNX
For the KNX world you need a Modul at the Raspberry Pi to connect as an Actor 
The execute only sends an value to a given Group e.g

```
0/0/1 1 
```

In the background it sends the command to the System

```
knxtool groupswrite ip:localhost 0/0/1 1
```


###PHue
For the Philip Hue look at the official Documentation for Phillips Hue
###Modbus 
At the modbus-test folder are two file for Testing the Modbus System