from colorama import Fore
from pystyle import Center
import os
import random
import requests
import json

titlelogs = "Wallet-Finder - By Chakal#0001 & Deus"
caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
banner = (f"""
| Wallet Finder | 1.0
|══════════════════════════════════════════════
| By Chakal#0001 & DEUS-WEB
| Discord : .gg/UGEMWmZYjp
|══════════════════════════════════════════════
| Welcome to Wallet-Finder.
""")

wallet = (f"""

                                 ██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗   ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
                                 ██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝   ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
                                 ██║ █╗ ██║███████║██║     ██║     █████╗     ██║█████╗█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
                                 ██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
                                 ╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║      ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
                                  ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                   
                                                                         -> BY Chakal#0001 & Deus
                                                                                                                         
""")


def loading():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "Wait....")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(wallet)
    input('Press ENTER to start.')

loading()


while True:
    pvkeybt = ''
    for i in range(42):
        pvkeybt = f"{pvkeybt}{random.choice(caracteres)}"
    balance = requests.get(
        "https://blockchain.info/balance?active=" + pvkeybt).text
    sltcv = json.loads(balance)

    if 'message' in sltcv:
        print(Fore.RED + "                                              [" + Fore.GREEN + "!" + Fore.RED + "] " + "Private key " + Fore.MAGENTA +
                    pvkeybt + Fore.GREEN + " Balance " + Fore.YELLOW + '0.00000 BTC')
        
    elif sltcv[pvkeybt]['final_balance'] > 0.00001:
        prefin = str(sltcv[pvkeybt]['final_balance'])
        y = prefin[0:2] + "," + prefin[2:7]
        print(Fore.RED + "                                              [" + Fore.GREEN + "!" + Fore.RED + "] " + "Private key " + Fore.YELLOW +
              pvkeybt + Fore.GREEN + " Balance " + Fore.YELLOW + y + ' BTC')
        choice = input(Center.XCenter('Save & continue [y/n] >'))

        if choice == 'y':
            keybdhit = open("hit.txt", "a+")
            keybdhit.write(f"{pvkeybt}\n")
            keybdhit.close()

        elif choice == 'n':
            exit()