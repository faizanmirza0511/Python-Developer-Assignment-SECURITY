import os
import subprocess
import ctypes
import re
import time


#Blocking USB Ports and Disabling Bluetooth:

# Import necessary module for WMI
import wmi

# Connect to WMI
wmi_connection = wmi.WMI()

# Disable USB devices
def disable_usb_ports():
    usb_devices = wmi_connection.query("SELECT * FROM Win32_USBControllerDevice")
    for device in usb_devices:
        # Disable the device
        device_path = device.Dependent.DeviceID
        wmi_connection.Win32_PnPEntity(DeviceID=device_path)[0].Disable()

# Disable Bluetooth
def disable_bluetooth():
    # Code to disable Bluetooth using WMI or other suitable methods
    pass

# Call the functions to disable USB ports and Bluetooth
disable_usb_ports()
disable_bluetooth()



# Disabling Command Prompt:
def disable_command_prompt():
    # Code to modify the registry to disable the command prompt
    pass

disable_command_prompt()



# Blocking Website Access:
def block_website(website):
    hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_file_path, "a") as hosts_file:
        hosts_file.write(f"127.0.0.1 {website}\n")

website_to_block = "facebook.com"
block_website(website_to_block)



# Optional: Executable File:
pip install pyinstaller
pyinstaller --onefile security_manager.py
