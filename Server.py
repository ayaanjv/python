#server.py
import socket
host='192.168.0.14'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host, port))
print('socket binded to', port)

backlog = 5
s.listen(backlog)

conn,addr = s.accept()
print ('socket is listening')
print ("Got connection from",addr)

while 1:
    name=input('Hello, say something to the client')
    print("waiting for client's response")
    conn.send(name.encode())
    data=conn.recv(1024).decode('utf-8')
    print('Received from client address: ', addr)
    print("Message received: ",data)
conn.close()


#Try it on two different devices
#put client code on py and other on mac
#Build pygame multiplayer
