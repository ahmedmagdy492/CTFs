#!/usr/bin/python3
import os
import requests

result = requests.patch("http://mercury.picoctf.net:28916/")
os.system("echo '%s' > sample.html" % result.content.decode('utf8'))