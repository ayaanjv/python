from TicTacToeMenu import *
from PongMenu import* 
import time
import pygame
from pygame.locals import*
pygame.init()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white  = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption ('GAME Menu')

def st(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',70)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))
def text(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',150)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))

def  button():
     pygame.draw.rect(screen,green,(0,300, 290,600),10)
     pygame.draw.rect(screen,red,(600,300, 295,600),10)
     pygame.draw.rect(screen,blue,(300,300,290,600),10)
    

   
while True :
    button()
    st('Tic',85,510,green)
    st('Tac',85,590,green)
    st('Toe',85,660,green)
    st('Quit',675,540,red)
    st('Pong',365,540,blue)           
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y=event.pos
            if x >0 and x < 300 and y  > 300 and y < 900:
                text('Tic Tac Toe',70,150,white)
                pygame.display.update()
                screen.fill(black)
                time.sleep(1)
                menu()
                x=0
                y=0
            if x >300 and x < 600 and y  > 300 and y < 900:
                text('Pong',300,150,white)
                pygame.display.update()
                screen.fill(black)
                time.sleep(1)
                pong()
                x=0
                y=0
              

            if x >600 and x<900 and y>300 and y< 900:
                text('Quit',300,150,white)
                pygame.display.update()
##                quit()
                    

             



    
  
 
