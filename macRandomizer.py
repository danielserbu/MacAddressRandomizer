#!/usr/bin/env python

import subprocess
import random
import time

def get_current_mac_address():
	mac_address = str(subprocess.check_output("ifconfig " + interface, shell=True)).partition("ether")[2][1:18]
	return mac_address

interface = input("interface > ")
new_random_mac = "%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255),
                                             random.randint(0, 255),
                                             random.randint(0, 255),
                                             random.randint(0, 255),
                                             random.randint(0, 255),
                                             random.randint(0, 255))

print("Changing MAC address for " + interface + " interface to " + new_random_mac)

previous = get_current_mac_address()
print("Previous MAC Address: " + previous)

#Change MAC address
subprocess.call("ifconfig " + interface + " down", shell=True)
time.sleep(5)
subprocess.call("ifconfig " + interface + " hw ether " + new_random_mac, shell=True)
time.sleep(5)
subprocess.call("ifconfig " + interface + " up", shell=True)

after = get_current_mac_address()
print("After MAC Address: " + after)

if (previous == after):
	print("[-] MAC Address Change Failed")
else:
	print("[+] MAC Address Change Successful")