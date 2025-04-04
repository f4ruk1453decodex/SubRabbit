# SubRabbit V1.0
# Subdomain Scanner Tool
# by TFX1337
# ig : invisible_turnstile

import os
import socket
from multiprocessing.dummy import Pool
from colorama import init, Fore
import pystyle
import argparse

init()
print("\n")
banner = Rf'''                              __
                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'        {Fore.LIGHTWHITE_EX} ________      ______ ________       ______ ______ __________ 
       .--""""--..__/     `.       {Fore.BLUE} __  ___/___  ____  /____  __ \_____ ___  /____  /____(_)_  /_
     .'           .'    `o  \       {Fore.LIGHTWHITE_EX}_____ \_  / / /_  __ \_  /_/ /  __ `/_  __ \_  __ \_  /_  __/
    /                    `   ;     {Fore.BLUE} ____/ // /_/ /_  /_/ /  _, _// /_/ /_  /_/ /  /_/ /  / / /_  
   :                  \      :    {Fore.LIGHTWHITE_EX} /_____/ \__,_/ /_.___//_/ |_| \__,_/ /_.___//_.___//_/  \__/  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;        {Fore.LIGHTWHITE_EX}IG : {Fore.RED}@{Fore.LIGHTWHITE_EX}invisible_turnstile
'._:           ;   :   (         {Fore.LIGHTWHITE_EX}TG : {Fore.RED}@{Fore.LIGHTWHITE_EX}TFX1337
    \/  .__    ;    \   `-.     {Fore.LIGHTGREEN_EX} SubRabbit is fastest subscanner tool
     ;     "-,/_..--"`-..__)     {Fore.LIGHTWHITE_EX}Total Subdomains : 789.826
     '""--.._:

'''
print(pystyle.Colorate.Vertical(pystyle.Colors.red_to_yellow, banner))




try:
    with open("subdomains.txt", "r") as f:
        subdomains = f.read().splitlines()
except FileNotFoundError:
    print(f"{Fore.LIGHTWHITE_EX}[{Fore.RED}x{Fore.LIGHTWHITE_EX}] Not Found : subdomains.txt")
    exit()

def check_dns(sub):
    domain = f"{sub}.{TARGET_DOMAIN}"
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.GREEN}+{Fore.LIGHTWHITE_EX}] SUCCESS {Fore.YELLOW}|{Fore.LIGHTWHITE_EX} {domain}")
        with open(os.path.join(f"subdomains_{TARGET_DOMAIN}.txt"), "a") as f:
            f.write(f"{domain}\n")
    except socket.gaierror:
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.RED}-{Fore.LIGHTWHITE_EX}] INVALID {Fore.YELLOW}|{Fore.LIGHTWHITE_EX} {domain}")

def main():
    global TARGET_DOMAIN

    parser = argparse.ArgumentParser(description="SubRabbit - Subdomain Scanner")
    parser.add_argument("-t", "--target", help="Target domain")
    parser.add_argument("-l", "--list", help="Target list file")
    args = parser.parse_args()
    print("-l / --list : Scan from list ")
    print("-t / --target : Scan url ")
    targets = []

    if args.target:
        targets = [args.target.strip()]
    elif args.list:
        if not os.path.exists(args.list):
            print(f"{Fore.LIGHTWHITE_EX}[{Fore.RED}x{Fore.LIGHTWHITE_EX}] Not Found : {args.list}")
            return
        with open(args.list, "r",encoding="UTF-8") as f:
            targets = [line.strip() for line in f if line.strip()]

    for domain in targets:
        print(f"\n{Fore.LIGHTWHITE_EX}[{Fore.CYAN}~{Fore.LIGHTWHITE_EX}] Scan Started : {Fore.YELLOW}{domain}")
        TARGET_DOMAIN = domain
        with Pool(100) as pool:
            pool.map(check_dns, subdomains)
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.GREEN}+{Fore.LIGHTWHITE_EX}] Scan Is Completed : {domain} ")

if __name__ == "__main__":
    main()
