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


###PHue
###Modbus 