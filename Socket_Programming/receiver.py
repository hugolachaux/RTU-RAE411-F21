#Merwane LE MOIGNE
#IPSA Paris

import socket
IP="127.0.0.1"
PORT=54321
sock=socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM)
sock.bind((IP,PORT))
data,addr=sock.recvfrom(1024)

print("sender : ",addr)
print("data   : ",data.decode('utf-8'))






