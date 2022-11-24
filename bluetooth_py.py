#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function  # import print from python3: end=""
import time
import re
import pexpect  # sudo apt-get install python-pexpect
import subprocess
import random
import bluetooth
def createServer():
   

    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    data=1
    port = 1
    server_sock.bind(("",port))
    server_sock.listen(1)

    client_sock,address = server_sock.accept()
    print("Accepted connection from ",address)
    
    while data != str(b'quit\r\n'):
        data = str(client_sock.recv(1024))
        print(data)

    client_sock.close()
    server_sock.close()   


createServer()
    


    

