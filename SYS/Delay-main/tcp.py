import socket
import time

class Samsung_control():
# client.connect((target, port))

    def Samsung_On():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.10.131', 1515))
        client.send(b'\xAA\x11\xFE\x01\x01\x11')
        #response = client.recv(4096)
        #print(response)
        print("TV on")

    def Samsung_Off():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.10.131', 1515))
        client.send(b'\xAA\x11\xFE\x01\x00\x10')
        #response = client.recv(4096)
        #print(response)
        print("TV off")
   
class VLC_control():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def test():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.10.130', 50000))
        response = client.recv(4096)
        print(response)
        print("Connected to VLC")
    
    def msg():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.10.130', 50000))
        time.sleep(1)
        client.send(b'add rtsp://admin:ms1234@192.168.10.10:554/' + b'\r\n')
        response = client.recv(4096)
        client.send(b'play' + b'\r\n')
        time.sleep(2)
        client.send(b'f on' + b'\r\n')
        print(response)
        print("Talk to VLC")
    
    def slower():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 50000))
        time.sleep(1)
        client.send(b'slower' + b'\r\n')
        response = client.recv(4096)
        #client.send(b'play' + b'\r\n')
        #time.sleep(2)
        #client.send(b'f on' + b'\r\n')
        #print(response)
        print("slower")
        
    def normal():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 50000))
        time.sleep(1)
        client.send(b'normal' + b'\r\n')
        response = client.recv(4096)
        #client.send(b'play' + b'\r\n')
        #time.sleep(2)
        #client.send(b'f on' + b'\r\n')
        #print(response)
        print("slower")
        
        
