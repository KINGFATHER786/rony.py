#!/bin/python3.10
# coding _-_udf:8_-_
# made by : Bilal Haider ID
from os import system as cmd
from sys import argv as arg
from time import sleep as slp
from requests import get as get
from random import choice
from pathlib import Path
import requests,random,sys,json,os,re,string
import sys,platform,os,time
green = "\x1b[1;92m"
red = "\x1b[1;91m"
white = "\x1b[1;97m"
hijau  ="\x1b[1;92m"
cyan   ="\x1b[1;96m"
kuning ="\x1b[1;93m"
ungu   ="\x1b[1;95m"
putih  ="\x1b[1;97m"
biru   ="\x1b[1;94m"
merah  ='\x1b[1;91m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
def logo():
	print("""
     
+────────────────────────────────────────────────+
  Author :- Faraz Ali ID
  Github :- FARAZ-ID
  Note   :- Get Detail Of Pakistan Number
+────────────────────────────────────────────────+       """)                              
def mobile_info():
	os.system("clear")
	logo()
	print("[*] Enter Number Without Country Code and 0 ")
	print("[*] For Example : 3445440995 etc")
	print("-"*50)
	nmbr = input("[->] Target Mobile Number  : ")
	head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded',"Referer": "https://freepicccs.com/index2.php?msg=Please%20Enter%20atleast%201%20Mobile%20Number%20or%20CNIC"}
	dataa = {'cnnum': nmbr}
	r = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=dataa)
	bc = re.findall("\<div(.*?)</table>",str(r.text))
	open("t.txt","w").write(str(bc))
	bx = open("t.txt","r").read()
	z = """[' style="margin-top:10px" class="col-lg-12 bg-danger text-white text-center" >Record 1 </div><table><tbody><tr><td>"""
	bx = bx.replace("</td><td>","").replace("</td></tr><tr><td>","").replace("<strong>","<X>").replace("</strong>","<X>").replace(z,"").replace("</td></tr></tbody>","")
	bx = bx.split("<X>")
	print("-"*50)
	try:print(f"[*] {bx[0].capitalize()} : {bx[1]}")
	except:pass
	try:print(f"[*] {bx[2].capitalize()} : {bx[3]}")
	except:pass
	try:print(f"[*] {bx[4].capitalize()} : {bx[5]}")
	except:pass
	try:print(f"[*] {bx[6].capitalize()} : {bx[7]}")
	except:pass
	try:print(f"[*] {bx[8].capitalize()} : {bx[9]}")
	except:pass
	try:print(f"[*] {bx[10].capitalize()} : {bx[11]}")
	except:pass
	try:print(f"[*] {bx[12].capitalize()} : {bx[13]}")
	except:pass
	print("-"*50)
	input("[*] Press Enter to go Back :/")
	mobile_info()
	
if __name__=='__main__':
	mobile_info()