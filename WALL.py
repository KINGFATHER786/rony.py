from urllib import response

import mechanize
from os import path
import os
import requests
import datetime

import sys

from time import sleep
ah="TRICKER-"
imt="-M4786=="
ak=" H9SS9N-"


def faraz():
  print("""  \033[1;92m 
  \033[1;97m
  \033[1;92m
  \033[1;97m 
  \033[1;92m
  \033[1;97m                                                  
@@@@@@@   @@@@@@@    @@@@@@   @@@  @@@  @@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@!  @@@  @@!@!@@@  @@!  @@@  
!@   @!@  !@!  @!@  !@!  @!@  !@!!@!@!  !@!  @!@  
@!@!@!@   @!@!!@!   @!@!@!@!  @!@ !!@!  @!@  !@!  
!!!@!!!!  !!@!@!    !!!@!!!!  !@!  !!!  !@!  !!!  
!!:  !!!  !!: :!!   !!:  !!!  !!:  !!!  !!:  !!!  
:!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  
 :: ::::  ::   :::  ::   :::   ::   ::   :::: ::  
:: : ::    :   : :   :   : :  ::    :   :: :  :                                                                                                       
\033[1;97m====================================================
\033[1;97m[+]\033[1;91m    AUTHOR   \033[1;90m: \033[1;92mH4SS4N X3 W9SIF
\033[1;97m[+]\033[1;91m    FACEBOOK \033[1;90m: \033[1;92mM.Hassan
\033[1;97m[+]\033[1;91m    WHATSAPk \033[1;90m: \033[1;92m+923272458382
\033[1;97m====================================================
\x1b[31;1m   \x1b[47;2m[ THIS TOOL IS FREE ]\x1b[00;1m\x1b[31;1m \x1b[31;1m \x1b[47;2m[ POWERED BY HUNT3R X3 H4SS4N ]\x1b[00;1m\x1b[31;1m
\033[1;97m====================================================""")

os.system("clear")
faraz()
	
	
browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)
    
    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣Entar Two Factor Code On Athenticator App : "))

    print(msg1)

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()

    

#faraz()

    

def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()

print ("[-[ CR3AT3D BY WASIIF X3 H9SS9N  ]-]")

emailx=str(input("➣Entar Email : "))

pwx =str(input("➣Entar Pass : "))

aclass()

msg4=str(input("➣P0ST LIINK : "))

msg5=str(input("➣Entar Abuse File Path : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Time limit : "))

os.system('clear')

sys.stdout.flush()

print('kbaad v1.0')

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(line)

            print('Comment Done - ', line)

            count += 1

            if count % 10 == 0:

                sleep(1)

                

