#coded_by_solo_hacker
"""
Don't Use Without
Credits
"""
import itertools, threading, time, sys, os
import requests
import rich
import json,os,sys,random,datetime,time,re
from concurrent.futures import ThreadPoolExecutor as speed
from rich.markdown import Markdown as mark
from rich import pretty
from random import choice as pilih
P = '\x1b[0;97m'
M = '\x1b[0;91m' 
H = '\x1b[0;92m' 
K = '\x1b[0;93m'
B = '\x1b[0;94m'
U = '\x1b[0;95m' 
O = '\x1b[0;96m' 
N = '\x1b[0m'   
I='\x1b[0;32m'
C='\x1b[0;36m'
M='\x1b[0;31m'
U='\x1b[0;35m'
K='\x1b[0;33m'
P='\x1b[00m'
H='\x1b[0;90m'
Q="\x1b[00m"
i='\x1b[0;32m'
c='\x1b[0;36m'
m='\x1b[0;31m'
u='\x1b[0;35m'
k='\x1b[0;33m'
b='\x1b[0;34m'
p='\x1b[00m'
h='\x1b[0;90m'
q="\x1b[00m"
pretty.install()
ses=requests.Session()
def soloflash(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
        
def soloflashlogo(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
id,uid= [],[]
linex = ('\033[0;97m═══════════════════════════════════════════════')

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # mix
m = '\x1b[1;91m' #lal +
k = '\033[93m' # pila +
h = '\x1b[1;92m' # hara +
hh = '\033[32m' # hara2 -
u = '\033[95m' # gulabai
kk = '\033[33m' # pila2 -
b = '\33[1;96m' # surkh -
p = '\x1b[0;34m' # halka nila +
sziloveyu = random.choice([U,I,K,h,hh,U,u,m,k,h,u,b])



def sz__love(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    try:
        os.system('clear')
    except KeyError or IOError:
        os.system('cls')
def sologo():
	clear()
	soloflashlogo(f'{sziloveyu}   ▄████████    ▄█    █▄     ▄██████▄  \n  ███    ███   ███    ███   ███    ███ \n  ███    █▀    ███    ███   ███    ███\n  ███         ▄███▄▄▄▄███▄▄ ███    ███ [S]\n▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ [O]\n         ███   ███    ███   ███    ███ [L]\n   ▄█    ███   ███    ███   ███    ███ [O]\n ▄████████▀    ███    █▀     ▀██████▀  ')
	soloflashlogo(f'{linex}\n Author    : SOLOO HACKER\n Version   : 4.3\n Github    : solohackerzorganization \n{linex}\n\t\tMain Menu')
def check_login():
	try:
		token = open('solotoken.txt','r').read()
		cok = open('solocok.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+token, cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except :login()
	except requests.exceptions.ConnectionError:
		li = 'Connection Problem'
		lo = mark(li, style='red')
		sol().print(lo, style='purple')
		exit()
	except IOError:
		login()

def login():
 try:
  clear()
  print('') 
  ses = requests.Session();sologo();print(linex)
  cookie = input('\nEnter Facebook Cookies : ')
  cookies = {'cookie':cookie}
  url = 'https://www.facebook.com/adsmanager/manage/campaigns'
  req = ses.get(url,cookies=cookies)
  set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
  nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
  roq = ses.get(nek,cookies=cookies)
  tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
  tokenw = open("solotoken.txt", "w").write(tok)
  cokiew = open("solocok.txt", "w").write(cookie)
  soloflash(f'{linex}\nLogin SuccessFull\n ')
  check_login()
 except Exception as e:
  os.system("rm -f solotoken.txt")
  os.system("rm -f solocok.txt")
  print(f' Login Failed (May be Cookies are Expired)')
  exit()	
#------------------[ BAGIAN-MENU ]----------------#
def menu(sy2,sy3):
	try:
		tok = open('solotoken.txt','r').read()
		cok = open('solocok.txt','r').read()
	except ValueError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		check_login()
	clear()
	sologo()
	ip = requests.get("https://api.ipify.org").text
	sz__love(f'{linex}\n\x1b[1;37m>> IP    : {ip}');sz__love(f'\x1b[1;37m>> Name  : {sy2}');sz__love(f'\x1b[1;37m>> UID   : {sy3}\n{linex}')
	print('[1] Create Super File (Unlimited)')
	print('[2] Remove Double Links')
	print('''[3] Seperate New ID's Links''')
	print('''[4] Removing Part of File''')
	print('''[5] Contact Owner''')
	print('''[6] Remove Cookies''')
	print('''[0] Exit''')
	soloin = input(f'{linex}\n>> Select : ')
	print('')
	if soloin in ['1' or '01']:
		filename()
	elif soloin in ['2' or '02']:
		remove_double()
	elif soloin in ['3' or '03']:
		sorting_file()
	elif soloin in ['4'or'04']:
		part_remove()
	elif soloin in ['5' or '05']:
		contact_author()
	elif soloin in ['6' or '06']:
		rem_login()
	elif soloin in ['0' or '00']:
		soloflash('Thanks For Using My Tool')
	else:
		errorz()
def errorz():
	soloflash(f'{k}>>Please Choose Correct Option {x}')
	time.sleep(3)
	check_login()
def rem_login():
	os.system('rm -rf sol*')
	soloflash('Cookies SucessFully Removed')

#===========Filename
def filename():
    clear();sologo()
    soloflash(f'{linex}\nExample : /sdcard/solofile.txt')
    filen=input(f'{linex}\nEnter File Path : ')
    superfile(filen)
#-------------------[ CRACK-PUBLIK ]-------------
###################################
def superfile(filen):
	try:token = open('solotoken.txt','r').read();cok = open('solocok.txt','r').read()
	except IOError:exit()
	kil = input(f'{linex}\nEnter Link of Public ID : ');clear();sologo()
	uid.append(kil);print(f'{linex}\nDumping Started \nPress Ctrl+Z to stop\n{linex}\nFile Will be Saved in {filen}\n{linex}')
	cookie_dict = {}
	for cookie in cok.split(';'):name, value = cookie.strip().split('=', 1);cookie_dict[name] = value
	ciik = json.dumps(cookie_dict)
	headers = {
    'authority': 'graph.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
	}
	params = {
    'access_token': token,
    'limit': '5000',
	}	

	for userr in uid:
		try:
			lilis = requests.get(f'https://graph.facebook.com/{kil}/friends',params=params,cookies=cookie_dict,headers=headers)
			linkdump = json.loads(lilis.text)
			for appui in linkdump['data']:
				try:
					soloid = (appui['id']+'|'+appui['name'])
					if soloid in id:pass
					else:id.append(soloid)
					zxx=open(filen, "a+").write(soloid+'\n');zxx.close()
				except:pass
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Network Error ')
			exit()
	try:
		with speed(max_workers=20) as (solohacker):
			juma = open(filen,"r").readlines()
			for data in juma:
				data = data.replace("\n","")
				kiky = data.split("|")
				useriid = ("%s"%(kiky[0]))
				nm = ("%s"%(kiky[1]))
				solohacker.submit(multi_file, useriid,filen)

	except requests.exceptions.ConnectionError:
		print(f'{x}')
		soloflash('>> Network Error ')
		check_login()
	except (KeyError,IOError):
		soloflash(f'>>{k} This is Private Account {x}')
		time.sleep(3);check_login()
#============================
xz = []
def multi_file(useriid,filen):
	try:token = open('solotoken.txt','r').read();cok = open('solocok.txt','r').read()
	except IOError:exit()
	cookie_dict = {}
	for cookie in cok.split(';'):name, value = cookie.strip().split('=', 1);cookie_dict[name] = value
	ciik = json.dumps(cookie_dict)
	headers = {
    'authority': 'graph.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
	}
	params = {
    'access_token': token,
    'limit': '5000',
	}
	try:
		li = requests.get(f'https://graph.facebook.com/{useriid}/friends',params=params,cookies=cookie_dict,headers=headers)
		linkdump =json.loads(li.text)
		for appui in linkdump["data"]:
				try:
					soloid = (appui["id"]+'|'+appui["name"])
					if soloid not in id:id.append(soloid);xaz=open(filen,'a+');xaz.write(soloid+'\n');xaz.close()
					else:pass
				except:pass
	except KeyError:pass
	
	sys.stdout.write("\r%s[%sExtracted Accounts ]%s •> %s"%(Q,pilih([U,I,K,h,M,C]),Q, len(id))); sys.stdout.flush()
#============================
def remove_double():
    clear();sologo()
    soloflash(linex)
    file = input ('\033[0;92m Enter Your File Path : ')
    soloflashlogo(linex)
    os.system(f'sort -u -r -o {file} {file} --quit 2>/dev/null')
    print ('\n[*] SuccessFully Removed Double Links')
    print ('[*] File Saved in : '+file)
    input(f'{linex} \nPress Enter to go back to Main Menu')
    clear()
    check_login()
    
def sorting_file():
    clear();sologo()
    soloflashlogo(linex)
    try:linkslimit = int(input(' How many links do you want to Seperate : '))
    except:linkslimit = 1
    soloflashlogo(f'{linex}\nPlease Enter File Path\nExample: /sdcard/mfile.txt')
    file = input (f'{linex}\nInput Your File Path : ')
    fileout = input(f'Where Do you want to save the File : ')
    y = 0
    soloflashlogo(f"{linex}\n Links You Want To Keep\nExample : [100088,100089,100090etc]")
    os.system('rm -rf 1.txt');os.system('rm -rf .solo.txt')
    for k in range(linkslimit):y+=1;links=input('Put Links : ');os.system('cat '+file+' | grep "'+links+'" >> '+fileout+' --quiet 2>/dev/null')
    os.system(f'sort -u -r -o {fileout} {fileout} --quit 2>/dev/null')
    soloflashlogo(f'{linex}\n Accounts SuccessFully Extracted');print(' Total Accounts Extraced : '+str(len(open(fileout,'r',encoding='utf-8').read().splitlines())))
    print('\033[0m New Accounts File saved in : \033[0;32m'+fileout)
    input(f'{linex}\nPress Enter to go back to Main Menu')
    clear()
    check_login()
#=====================
def part_remove():
    clear();sologo()
    soloflashlogo(f'''{linex}\nType (solo) if you want help''')
    soloflashlogo(f'''{linex}\nExaple : newfile.txt''')
    soloinput1 = input(f'{linex}\nEnter The File You Want To Remove Part of :')
    if ('solo' or 'Solo'or '(solo)' or 'SOLO') in soloinput1:
        contact_author()
    else:
        soloflashlogo(f'{linex}\nExample : If You want to remove first \n1000 lines enter : 1000')
        xasi = input(f'{linex}\nHow Much Lines of File do you want to Remove:')
        os.system('sed -i 1,'+xasi+'d '+soloinput1)
        soloflashlogo(f'{linex}\nYour File is Saved in {soloinput1}\nFirst {xasi} lines are removed')
def contact_author():
	soloflashlogo('Wait! You Will Be redirected to author of the tool')
	os.system('xdg-open https://wa.link/ozyc9p')
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('rm -rf ..solo.txt')
	except:pass
	try:os.system('rm -rf .solo.txt && rm -rf tmp')
	except:pass
	os.system('rm -rf ..ijs.txt')
	check_login()