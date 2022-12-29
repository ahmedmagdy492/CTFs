#!/bin/python3

import os

#passwordFileName = "/usr/share/set/src/fasttrack/wordlist.txt"
passwordFileName = "passwords.txt"

command = "steghide extract -sf cat.jpg -p %s"



with open(passwordFileName) as passFile:
    curPassword = passFile.readline()
    while(curPassword):
        print("-"*50)
        print("testing with password: %s" % curPassword)
        os.system(command % curPassword)
        curPassword = passFile.readline()

