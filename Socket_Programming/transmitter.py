#Merwane LE MOPIGNE
#IPSA Paris

import socket

IP="127.0.0.1"
PORT=54321
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data=input("Enter a text")

sock.sendto(data.encode('utf-8'),(IP,PORT))





