import os, platform

import requests

from os import system as cmd

os.system('git pull')
bit = platform.architecture()[0]

if bit == '64bit':

    from Mani import Main

    Main()