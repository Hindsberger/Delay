import socket
from sys import *
import binascii


msg       = "xaa\x11"
bytesToSend1         = binascii.hexlify(b'\xAA\x11\xFE\x01\x01\x11', ' ')
#bytesToSend         = b'\aa\x11\xfe\x01\x01\x11' #Tænd
#bytesToSend         = b'\xaa\x11\xfe\x01\x00\x10'
#print(bytesToSend)
#d = b'\xAA\x11\xFE\x01\x01\x11'
#test ="".join(["{:02x}".format(x) for x in d])
#var = b'\xAA\x11\xFE\x01\x01\x11'
#bytesToSend2 = b'\xAA\x11\xFE\x01\x01\x11' #Tænd
bytesToSend2 = b'\xAA\x11\xFE\x01\x00\x10' #Sluk
#print(b"%X" % 170, "11", "%X" % 254, "01", "01", "11")
#print('\x%A\x11\xFE\x01\x01\x11' % "AA")
#print(hex(var))
#print(test)
print(bytesToSend1)
print(bytesToSend2)

serverAddressPort   = ("192.168.10.131", 1515)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

#UDPClientSocket.sendto(bytesToSend1, serverAddressPort)
UDPClientSocket.sendto(bytesToSend2, serverAddressPort)

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
