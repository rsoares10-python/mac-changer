#!/usr/bin/env python

# Built-in/Generic Imports
import subprocess
import optparse
import re


def get_args():
    '''Get user arguments  and parse them.'''

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for more info")
    return options


def change_mac(interface, new_mac):
    ''' Change MAC address for a given interface.'''

    print("[+] Changing MAc address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    '''Search ifconfig output for MAC address using regex and return it.'''

    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(r"(\w{2}:)+\w{2}", ifconfig_output)
    if search_result:
        return search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


def check_mac(current_mac, new_mac):
    ''' Check if MAC address was successfuly changed.'''

    if current_mac == options.new_mac:
        print("[+] MAC address was successfuly changed to "+ current_mac)
    else:
        print("[-] MAC address did not get changed")


options = get_args()
current_mac = get_current_mac(options.interface)
print("Current MAC: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
check_mac(current_mac, options.new_mac)
