import pygame
import time
from pygame.locals import *
import socket
fpsclock=pygame.time.Clock()
pygame.init()
WIDTH=500
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("client")
red=(255,0,0)
blue=(0,0,255)
host='192.168.0.14'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host, port))



class Player:
    def __init__(self,color):
        self.x=WIDTH//2
        self.y=HEIGHT//2
        self.color=color
    def moveBy(self,x_distance,y_distance):
        self.x =self.x+ x_distance
        self.y =self.y+ y_distance
        
    def draw(self):
        pygame.draw.rect(window,self.color,(self.x,self.y,20,20))
player1=Player(red)
player2=Player(blue)
while True:
    fpsclock.tick(24)
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                player1.moveBy(0,-5)
            elif event.key==K_DOWN:
                player1.moveBy(0,5)
            elif event.key==K_LEFT:
                player1.moveBy(-5,0)
            elif event.key==K_RIGHT:
                player1.moveBy(5,0)
        
       
        
    player1.draw()
    s. send(bytes("{} {}\n".format(player1.x,player1.y),"utf-8"))
    data=s.recv(1024).decode('utf-8')

    data=data.strip()
    data=data.split()
##    print(data)
    player2.x=int(data[0])
    player2.y=int(data[1])
    player2.draw()
    pygame.display.update()
