# client.py
import socket
host=''  # server side ip address
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    data = s.recv(1024)  
    print('Received from server', repr(data))
    message=input("Say something to server: ")
    s.send(message.encode())
s.close()
