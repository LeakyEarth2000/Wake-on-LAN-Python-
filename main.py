# Wake on Lan via Python
# Created by Yash Batish (LeakyEarth2000)

# Prerequisites
    # pip install wakeonlan
    # pip install termcolor
# Sources
    # https://stackoverflow.com/questions/7629643/how-do-i-validate-the-format-of-a-mac-address  
    # https://pypi.org/project/wakeonlan/  
    # https://serverfault.com/questions/1018470/wol-and-wow-does-not-work-after-a-certain-time  
    # https://www.lifewire.com/wake-on-lan-4149800

import re
import ipaddress
from wakeonlan import send_magic_packet
from termcolor import colored

print("Hello there!")
print("This is a Wake on Lan app, where if you input your MAC address and IP Address of the computer you want to wake up, this app will allow you to wake them up")

# This section is the MAC Address. In short, this will determine whether the inputted MAC address is validated 
def validate_mac_address(ma):
    ma_lower = ma.lower()
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", ma_lower):
        print("MAC address is valid!")
        return ma_lower
    else:
        print(colored("Whoops, this won't work :/ \nPlease enter a valid MAC address. You can either seperate the hexadecimal character with a dash (-) or a colon (:)", "red"))
        return False
    
while True:
    x = input("\nEnter a MAC Address: ")
    validated_mac = validate_mac_address(x)
    if validated_mac:
        break

# This section is the IP Address. In short, this will determine whether the inputted IP address is validated and a private IP
def validate_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            print("Awesome! This is a private IP Address.")
            return True
        else:
            print(colored("This is a public IP address. Public IP addresses will not work here. You can obtain your Private IP via the command prompt -> ipconfig. It needs to also be IPV4", "red"))
            return False
    except ValueError:
        print(colored("Whoops, this doesn't seem to work :/ \nPlease enter a valid Private IPV4 address.", "red"))
        return False

# Get user input for the IP address
while True:
    print("\n")
    y = input("\nEnter a Private IP Address: ")
    if validate_private_ip(y):
        break

send_magic_packet(validated_mac, ip_address=y, port=1337)
print(colored("I have sent the Magic Packet! Your machine should be awake now.","light_green"))