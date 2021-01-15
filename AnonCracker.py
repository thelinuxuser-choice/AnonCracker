TGREEN =  '\033[92m' # Green Text

print(TGREEN +"    YOU DONOT BECOME A CODER BY JUST COPYING OTHER ONES CODES AND GET CREDITS TO YOU!   ")
# THIS IS A PYTHON  CODE TO DEVELOP YOUR BRAIN WITHOUT MUSCLES
# I FORGOT THIS IS A CASE SENSITIVE LANG AND I TYPED Print else writing print _XD lol!
bold='\033[01m'
TGREEN = '\033[92m' # Green Text
WARNING = '\033[93m' #nothing
FAIL = '\033[91m' #just shut up


print(WARNING+bold+"   ('-.         .-') _                   .-') _             _   .-')                               .-') ")
print(WARNING+bold+"  ( OO ).-.    ( OO ) )                 ( OO ) )           ( '.( OO )_                            ( OO ).")
print(WARNING+bold+"  / . --. /,--./ ,--,'  .-'),-----. ,--./ ,--,'  ,--.   ,--.,--.   ,--.).-'),-----.  ,--. ,--.   (_)---\_)")
print(WARNING+bold+"  | \-.  \ |   \ |  |\ ( OO'  .-.  '|   \ |  |\   \  `.'  / |   `.'   |( OO'  .-.  ' |  | |  |   /    _ |")
print(WARNING+bold+".-'-'  |  ||    \|  | )/   |  | |  ||    \|  | ).-')     /  |         |/   |  | |  | |  | | .-') \  :` `.")
print(WARNING+bold+" \| |_.'  ||  .     |/ \_) |  |\|  ||  .     |/(OO  \   /   |  |'.'|  |\_) |  |\|  | |  |_|( OO ) '..`''.)")
print(WARNING+bold+"  |  .-.  ||  |\    |    \ |  | |  ||  |\    |  |   /  /\_  |  |   |  |  \ |  | |  | |  | | `-' /.-._)   \ ")
print(WARNING+bold+"  |  | |  ||  | \   |     `'  '-'  '|  | \   |  `-./  /.__) |  |   |  |   `'  '-'  '('  '-'(_.-' \       /")
print(WARNING+bold+"  `--' `--'`--'  `--'       `-----' `--'  `--'    `--'      `--'   `--'     `-----'   `-----'     `-----'")
print(FAIL+" ==========================================================================================================")
print(FAIL+" =    THIS IS A SCRET PYTHON SCRIPT TO   DEVELOP FREEKING HACKERS ABILITY BY A SCRIPT KIDDOS              =")
print(FAIL+" =          CODED BY PRABASH                                                                              =")
print(FAIL+" =    IF DID THIS HELP FOR YOU YOU CAN SIMPLY BY ME A COFFEE OR FOLLOW ME ON INSTA:=h3k3rs                =")
print(FAIL+" ==========================================================================================================")
print(TGREEN+"--------------THIS IS FOR EDUCATIONAL PURPOSE ONLY-I ALREADY WARNED YOU!---------------")
print(TGREEN +"                     ッ|simple bruteforce tool for     |ッ    ")
print(TGREEN +"                      ☺|pdf,hash,zip files superfast   | ☺   ")
print(TGREEN +"              ☠   ☠   ☠|donot use for illeagal purposes|☠  ☠  ☠  ")
print(TGREEN +"                    ----♛coming soon ssh bruteforcer♛------  \n")
print(TGREEN +"===================❌made with evil love❌====================================")
print(TGREEN +"=  ❌This Script Was Made By taj_0023 (thenga) and thelinuxuser-choice ❌        =")
print(TGREEN +"=  ❌[youtube coming soon - coming soon with full of love]❌                 = ")
print(TGREEN +"=        ❌[instergram - taj0023,thelinuxuser_choice]❌                                   = ")
print(TGREEN +"=============================================================================") 
print(" -Here is your operating system-                          ")
import os
print(os.system('uname -a'))         
print(TGREEN +"➊ SELECT NO 1 FOR PDF BRUTE FORCE ")
print("                             ")
print(TGREEN +"➋ SELECT NO 2 FOR ZIP BRUTE FORCE")
print("                             ")
print(TGREEN +"➌ SELECT NO 3 FOR HASH BRUTEFORCE")
print("                             ")


import subprocess as sub

option = input("1,2 or 3:")
if option == "1":
   filename = input(TGREEN +"ENTER YOUR FILE HERE=")
   wordlist = input(TGREEN +"ENTER YOUR WORDLIST HERE=")
   sub.run(f'python3 pdf.py {filename} {wordlist}'.split())
elif option == "2":
    filename = input(TGREEN +"ENTER YOUR FILE HERE=:")
    wordlist = input(TGREEN +"ENTER YOUR WORDLIST HERE=:")
    sub.run(f"python3 zip.py {filename} {wordlist}".split())
else:
   sub.run("python3 hash.py".split())


print(TGREEN +"THANK YOU!  ")
print(TGREEN +"STAY TUNED FOR NEW HACKING TOOLS")
print(TGREEN +"-------:GAME OVER:--------------")

