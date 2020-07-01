import random
# colors
yellow='\033[93m'
green='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+b+"""


            ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗
            ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
            ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║
            ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║
            ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║
            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝

                                                                        v 1.1
"""+b+red)

print (green+b+"              <===[[ coded by Anonymous-Srk ]]===>"+b+green)
print (" ")


length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))
print (" ")
print (yellow+b+"-----> password  generated <----"+b+yellow)
print (" ")
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_-@#$%&*^"
password= (green+b+" "+b+green)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> grab your password <----"+b+yellow)
print (" ")
