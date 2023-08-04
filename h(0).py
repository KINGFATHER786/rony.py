import os,sys,re,requests,time,json
from time import sleep as sp

ses = requests.Session()
def line():
	print(51*'-')
def logo():
	os.system("clear")
	print('''\033[1;97m
db       .d88b.   .d8b.  d8888b. d88888b d8888b. 
88      .8P  Y8. d8' `8b 88  `8D 88'     88  `8D 
88      88    88 88ooo88 88   88 88ooooo 88oobY' 
88      88    88 88~~~88 88   88 88~~~~~ 88`8b   
88booo. `8b  d8' 88   88 88  .8D 88.     88 `88. 
Y88888P  `Y88P'  YP   YP Y8888D' Y88888P 88   YD
-----------------------------------------------------------
 [•] Version  : 0.1
 [•] Github   : Dc Official
 [•] Author   : Aqib Ali
 [•] Facebook Loader Cp/File Tool ! 
-----------------------------------------------------------''')
#os.system("rm -rf /sdcard/respo.txt")
#cok = "datr=74BVZBYYnzwfMG9UyGHyLQOS;sb=74BVZIahpQ71u1wkYtHKkyOa;locale=en_GB;c_user=100075192622215;xs=6%3AgifIOL4RP6rY3g%3A2%3A1683391181%3A-1%3A8515;fr=0VycfqtDvi18Aq1Jp.AWX5yBFyB9bWd8590E_fqIxnaJE.BkVoLM.JD.AAA.0.0.BkVoLM.AWXjug8a_2c;zsh=ASTwHcQ2kKO8khe5ihcP4lI_eTvvBsMKTrnfXkaDbArwNeW733OU8x6Dwj5hQVfdvyFk3ruwoozzB08tsnR8ZKaQP6-upMz8mQ1_dj17Wq0nf73EW0W16jfiGsGsTjUfwm9GFMbjDaXirb6as5slLuYDmfEruItajX0obzHdzg925E6DTs0I2qFT0I2hwrMvpObYi-U4IgIL9fLT0gzuThUYVni3vSDkp8Bdx75qHAqWtxvieL82nEOk9j805CZg9e15oVUNvN6Hz9BlI_tfz5VMViX7GX8nKCluqFqrCkCdtOnosdvzzcpUVPwBN3T5RymO;m_page_voice=100075192622215;"

class main:
	def __init__(self):
		self.free = "https://d.facebook.com"
		#self.msg = " [•] Loader Started from Python server ! the unstoppable Legend Aqib InxiDe | Maria Randi ki Bahn Ko patak Patak kr chodonga , Maria ki chut fatgai  !!! "
	
	def menu(self):
		logo()
		try:
			cok = open(".loader_cookies.txt","r").read()
			token = open(".loader_token.txt","r").read()
		except FileNotFoundError:
			login()
		self.myid = cok.split("c_user=")[1]
		self.myid = self.myid.split(";")[0]
		#print(self.myid)
		cookies = {"cookie":cok}
		print(" [1] Facebook Messenger Loader (Multi IDs)\n [2] Facebook Post-Comments Loader (Multi IDs)\n [3] Facebook Messenger Loader (Free Fb)\n [4] Facebook Post-Comments Loader (Free Fb)\n [R] Remove Cookies ")
		m_1 = input(" [•] Choose : ")
		if m_1 == "1":
			self.freeMessengerMulti()
		elif m_1 == "2":
			self.freeCommentsMulti()
		elif m_1 == "3":
			self.freeMessenger(cookies)
		elif m_1 == "4":
			self.freeComments(cookies)
		elif m_1 in ['r','R']:
			os.system("rm -rf .loader_cookies.txt .loader_token.txt")
			login()
	
	def freeCommentsMulti(self):
		logo()
		cok = input(" [•] Put Cookies : ")
		cookies = {"cookie":cok}
		file= input(" [•] Put Loader Comments File : ")
		try:
			self.msg = open(file,"r").read()
		except FileNotFoundError:
			exit(" [•] Your File Not Found !!! ")
		line()
		self.target = input(" [•] Put Post Url : ")
		try:
			limit = int(input(" [•] How many Comments : "))
		except Exception as e:
			limit = 10
		print(" Ex: 1 , 0.01 , 0.009 Sec Etc ")
		try:
			delay = float(input(' [•] Put Delay Time :  '))
		except Exception as e:
			delay = float(1)
		
		try:
			r = requests.get(self.target,headers=cookies).text
		except Exception as e:
			exit(" [•] Cookies Expired Or Post Deleted !! ")
		except requests.exceptions.ConnectionError:
			exit(" [•] Please Check Your Internet !! ")
		data={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'comment_text': self.msg,})
		n=0
		for n in range(limit):
			try:
				sp(delay)
				comment_done = requests.post('https://d.facebook.com/a/comment.php?{}'.format(re.search('action="/a/comment.php\\?(.*?)"', str(r)).group(1).replace('amp;', '')), data = data, headers = cookies)
				print(f" [•] [{n+1}] Payload Commented  Successfully ")
			except requests.exceptions.ConnectionError:
				print(" [•] Please Check Your internet !! ")
				print(" [•] We Are Running Auto Session ! ")
				pass
			except Exception as e:
				print(e)
				exit(" [•] Cookies Expired Or Comments Blocked !! ")
		line()
		exit(" [•] Payload Comments Has been Finished !! ")
	def freeComments(self,cookies):
		logo()
		file= input(" [•] Put Loader Comments File : ")
		try:
			self.msg = open(file,"r").read()
		except FileNotFoundError:
			exit(" [•] Your File Not Found !!! ")
		line()
		self.target = input(" [•] Put Post Url : ")
		try:
			limit = int(input(" [•] How many Comments : "))
		except Exception as e:
			limit = 10
		print(" Ex: 1 , 0.01 , 0.009 Sec Etc ")
		try:
			delay = float(input(' [•] Put Delay Time :  '))
		except Exception as e:
			delay = float(1)
		try:
			r = requests.get(self.target,headers=cookies).text
		except Exception as e:
			exit(" [•] Cookies Expired Or Post Deleted !! ")
		except requests.exceptions.ConnectionError:
			exit(" [•] Please Check Your Internet !! ")
		data={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'comment_text': self.msg,})
		n=0
		for n in range(limit):
			try:
				sp(delay)
				comment_done = requests.post('https://d.facebook.com/a/comment.php?{}'.format(re.search('action="/a/comment.php\\?(.*?)"', str(r)).group(1).replace('amp;', '')), data = data, headers = cookies)
				print(f" [•] [{n+1}] Payload Commented Succesfully !! ")
			except requests.exceptions.ConnectionError:
				print(" [•] Please Check Your internet !! ")
				print(" [•] We Are Running Auto Session ! ")
				pass
			except Exception as e:
				print(e)
				exit(" [•] Cookies Expired Or Comments Blocked !! ")
		line()
		exit(" [•] Payload Comments Has been Finished !! ")
	
	
	def freeMessengerMulti(self):
		logo()
		cok = input(" [•] Paste Cookies : ")
		cookies = {"cookie":cok}
		file= input(" [•] Put Loader Msg File : ")
		try:
			self.msg = open(file,"r").read()
		except FileNotFoundError:
			exit(" [•] Your File Not Found !!! ")
		line()
		self.target = input(' [•] Paste Message Url : ')
		tid = self.target.split('tid=')[1]
		try:
			ids = tid.split('cid.c.')[1]
		except Exception as e:
			ids = tid.split('cid.g.')[1]
		tids = f'{tid}:{self.myid}'
		self.iAmLoader(cookies,ids,tids)
	def freeMessenger(self,cookies):
		logo()
		file= input(" [•] Put Loader Msg File : ")
		try:
			self.msg = open(file,"r").read()
		except FileNotFoundError:
			exit(" [•] Your File Not Found !!! ")
		#print(self.msg)
		line()
		self.target = input(' [•] Paste Message Url : ')
		tid = self.target.split('tid=')[1]
		ids = tid.split('cid.c.')[1]
		tids = f'{tid}:{self.myid}'
		self.iAmLoader(cookies,ids,tids)
	def iAmLoader(self,cookies,ids,tids):
		try:
			limit = int(input(' [•] Put Msg Limit : '))
		except Exception as e:
			limit = 10
		try:
			delay = float(input(' [•] Put Delay Time :  '))
		except Exception as e:
			delay = float(1)
		try:
			r = requests.get(self.target,cookies=cookies).text.replace("amp;","")
		except requsts.exceptions.ConnectionError:
			exit(" [•] Please Check your internet !  ")
		for x in re.findall('action\=\"(.*?)"',r):
			if 'messages/send/?' in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update({
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'tids':f'{tids}',
		'wwwupp':'C3',
		f'ids[ids]':f'{ids}',
		'platform_xmd':'',
		'referrer':'',
		'ctype':'',
		'cver':'legacy',
		'body':self.msg,
		'send':'Send'})
		n=0
		for n in range(limit):
			try:
				sp(delay)
				po = requests.post('https://d.facebook.com'+str(next),data=data,cookies=cookies).text.replace('amp;','')
				print(f" [•] [{n+1}] Msg Sent Succesfully !! ")
				line()
			except requsts.exceptions.ConnectionError:
				exit(" [•] Please Check your internet !  ")
		print(" [•] payload is finished !! ")



def login():
	logo()
	os.system("rm -rf .loader_cookies.txt .loader_token.txt")
	print(" [•] Use Only New Account ! ")
	print(" [•] Use at your own risk  ! ")
	line()
	print(" [1] Login Using Cookies ")
	print(" [2] Login Using Uid/Pass")
	line()
	log_menu = input(" [•] Select an Opt : ")
	if log_menu =="1":
		login_cookies()
	elif log_menu =="2":
		login_email_pw()

def login_cookies():
	logo()
	print(" [•] Use Only Kiwi Browser Cookies ")
	line()
	cok = input(" [•] Paste Cookies : ")
	cookies = {"cookie":cok}
	ses.headers.update(cookies)
	adheader = {'Host': 'adsmanager.facebook.com'}
	ses.headers.update(adheader)
	print(" [•] Validating Cookies !!! ")
	token = get_token()
	ses.headers.pop('Host')
	print(" [•] Acces Token : %s "%(token))
	open('.loader_cookies.txt','w').write(cok)
	open('.loader_token.txt','w').write(token)
	sp(2)
	main().menu()


def login_email_pw():
	logo()
	print(' [•] Use fresh new Account Dont Use Personal id')
	uid = input(' [•] Enter Uid : ')
	line()
	pw = input(' [•] Put Password : ')
	params = {
				"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": uid,
					"locale": "en_US",
					"password": pw,
					"sdk": "Android",
					"generate_session_cookies": "1",
					"sig": "62f8ce9f74b12f84c123cc23437a4a32"
				}
	headers = {
					"Host": "b-graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": 'Mozilla/5.0 (Linux; Android 4.2.0; vivo Y17 Build/JOP40C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0 Mobile Safari/90.0.4430.210 OPR/537.36 [FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + 'Zong' + ';FBMF/' + 'Vivo' + ' MOBILE LIMITED;FBBD/' + 'Vivo' + ';FBPN/com.facebook.katana;FBDV/' + 'Y17' + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"}
	q = ses.post("https://b-graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False).json()
	if "session_key" in q:
		coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
		cookie = f"sb={sb};{coki}"
		open('.loader_cookies.txt','w').write(cookie)
		print(' [•] Access Token : %s '%(q['access_token']))
		open('.loader_token.txt','w').write(q['access_token'])
		exit(' [•] Run Again ')
	else:
		exit(" [•] Your Account maybe on Chexkpoint !! ")

def get_token():
	url = "https://adsmanager.facebook.com/adsmanager/"
	try:
		r = ses.get(url=url).text
		get_act = re.search('act=(.*?)&nav_source',str(r)).group(1)
		get_link = ses.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={get_act}&nav_source=no_referrer").text
		tok = re.search('accessToken="(.*?)"',str(get_link)).group(1)
		return tok
	except:
		return(f"[x] Cookies Invalid ")


main().menu()

		