#!/usr/bin/python3
#creater:
#_________[ IMPORTING MODULES ]_______>>
import os,sys,json
import time,requests
#_________[ APP TOKEN ]_______>
app_token = "EAAGOfOcFdnYBAMZAAnqYaGYLy8qUMCgboBC4viDo1NataajrhTUUdv3eqETNCgq4iZCXdJnjZBIRMnFa8od2JzjQyUVdoXnw9HH9xFCvqsGH5KwjAXIZAXcrI9sB8S9OLBRN3ZCpdbDbYYYywdF6bN326e2n8LxDeZCMWUh2cV6ZAV4hdl6vx7K"
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
#_________[ LOGO ]______>>>
def logo():
    os.system("clear")
    print(f"""{white}
   __ _           _        __                  
  / _| |         (_)      / _|                 
 | |_| |__ ______ _ _ __ | |_ ___   __ _  __ _ 
 |  _| '_ \______| | '_ \|  _/ _ \ / _` |/ _` |
 | | | |_) |     | | | | | || (_) | (_| | (_| |
 |_| |_.__/      |_|_| |_|_| \___/ \__, |\__,_|
                                    __/ |      
                                   |___/ 
                          Creater : {green} Faraz Ali ID{white}
                          Version : {green}0.0.1{white}""")
    print(50*'-')
#_________[ PRINT JSON ]______>>>
def print_json_keys_values(json_data):
    for key, value in json_data.items():
        if isinstance(value, dict):
            print(f'[{green}+{white}] {key} : ')
            print_json_keys_values(value)
        else:
            print(f'[{green}+{white}] {key} : {value}')
#____________[ MAIN ]___________>>
def main():
    logo()
    uid = input(f"[{green}->{white}] Input fb uid : ")
    try:
        data = requests.get(f"https://graph.facebook.com/{uid}?metadata=1&access_token={app_token}").json()
    except Exception as e:
        print(f"\n {rad}Error : {e} {white}")
    print(50*'-')
    print_json_keys_values(data)
    print(50*'-')
    input(f" [{green}+{white}] Back / ")
    main()
if __name__=="__main__":
    main()