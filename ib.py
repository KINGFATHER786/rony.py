import os,sys, requests, re, random, time
from os import system as psl
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bsn
 
psl('rm -rf filer.txt')
idd = []
def logo():
    print("""\x1b[1;97md88888b  .d8b.  d8888b.  .d8b.  d88888D 
88'     d8' `8b 88  `8D d8' `8b YP  d8' 
88ooo   88ooo88 88oobY' 88ooo88    d8'  
88~~~   88~~~88 88`8b   88~~~88   d8'   
88      88   88 88 `88. 88   88  d8' db 
YP      YP   YP 88   YD YP   YP d88888P
-------------------------------------------
\033[;37m\033[;37mAuthor     :          Faraz Ali Jatoi
\033[;37m\033[;37mGithub     :          FARAZ-ID
\033[;37m\033[;37mVersion    :          0.1.0
\033[;37m\033[;37mTool Type  :          Spam
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
 
main()