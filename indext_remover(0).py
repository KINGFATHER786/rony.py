import os,time

#getting input of file location
try:
	file = input("file path : ")
except FileNotFoundError:
	exit(" Not Found File ")
except:
	exit("Something Wrong ! ")

#reading the content of input file
benzene = open(file,'r').read()

#if file have indext then process will start
if "    " in benzene:
	print("Collecting All Indext Spaces ....")
	time.sleep(2.7)
	#---(replacing-spaces)----#
	os.system(f"sed -i 's/    /	/g' {file}")
	os.system(f"sed -i 's/        /		/g' {file}")
	os.system(f"sed -i 's/            /			/g' {file}")
	os.system(f"sed -i 's/                /				/g' {file}")
	os.system(f"sed -i 's/                    /					/g' {file}")
	print("Completed Removing Indext ðŸ”¥ ")
	time.sleep(3)
	exit()
else:
	exit("This File Have No Indext Spaces To Remove .")
