from urllib import response
import mechanize
import os
import datetime
import sys
from os import path,system
from platform import uname
from time import sleep
from os import path
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*")



def logo():
	
   print("""  \033[1;92m 
  \033[1;97m__  __
  \033[1;92m/ / / /___ _______________ _____
  \033[1;97m/ /_/ / __ `/ ___/ ___/ __ `/ __ \   
  \033[1;92m/ __  / /_/ (__  |__  ) /_/ / / / /
  \033[1;97m/_/ /_/\__,_/____/____/\__,_/_/ /_/
\033[1;97m====================================================
\033[1;97m[+]\033[1;91m    AUTHOR   \033[1;90m: \033[1;92mIN4Y4T X3 H4SS4N
\033[1;97m[+]\033[1;91m    FACEBOOK \033[1;90m: \033[1;92mM.Hassan
\033[1;97m[+]\033[1;91m    WHATSAPk \033[1;90m: \033[1;92m+923272458382
\033[1;97m====================================================
\x1b[31;1m   \x1b[47;2m[ THIS TOOL IS FREE ]\x1b[00;1m\x1b[31;1m \x1b[31;1m \x1b[47;2m[ POWERED BY IN4Y4T X3 H4SS4N ]\x1b[00;1m\x1b[31;1m
\033[1;97m====================================================""")
def faraz():
	os.system('clear')
	logo()


##############################################
def logo():
	
   print("""  \033[1;92m 
  \033[1;97m__  __
  \033[1;92m/ / / /___ _______________ _____
  \033[1;97m/ /_/ / __ `/ ___/ ___/ __ `/ __ \   
  \033[1;92m/ __  / /_/ (__  |__  ) /_/ / / / /
  \033[1;97m/_/ /_/\__,_/____/____/\__,_/_/ /_/
\033[1;97m====================================================
\033[1;97m[+]\033[1;91m    AUTHOR   \033[1;90m: \033[1;92mIN4Y4T X3 H4SS4N
\033[1;97m[+]\033[1;91m    FACEBOOK \033[1;90m: \033[1;92mM.Hassan
\033[1;97m[+]\033[1;91m    WHATSAPk \033[1;90m: \033[1;92m+923272458382
\033[1;97m====================================================
\x1b[31;1m   \x1b[47;2m[ THIS TOOL IS FREE ]\x1b[00;1m\x1b[31;1m \x1b[31;1m \x1b[47;2m[ POWERED BY IN4Y4T X3 H4SS4N ]\x1b[00;1m\x1b[31;1m
\033[1;97m====================================================""")
def faraz():
	os.system('clear')
	logo()

		
	


        
url = 'https://m.facebook.com/login.php'
#"""
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        logo()
       
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)
       

	
	
def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    sp("Enter the 2 factor code by google authenticator : ")
    print("\033[1;37;40m")
    apr = str(input())
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("Your account got locked, recover it kindly and re run the script.")
        exit(1)
def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32;40m ")
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    print(">>", line, "")



os.system('clear')
logo()
print("\033[1;33;40m", end = "")
sp("Enter your email : ")
#print()
print("\033[1;37;40m")
USERNAME = str(input())
print("\033[1;33;40m", end = "")
sp("Enter your password :")
print("\033[1;37;40m")
PASSWORD = str(input())
login()
print("\033[1;34;40m", end = "")
sp("Enter chat group or inbox id link :\n")
print("\033[1;37;40m")
cid = str(input())
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
sp("Enter notepad file name :")
print("\033[1;37;40m")
np = str(input())
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
sp("Enter the time delay in seconds :\n")
print("\033[1;37;40m")
t = int(input())

clear()

os.system('clear')

logo()
	

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
                logo()
                

    
main()                