from TICTACTOE import *
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
pygame.display.set_caption ('tic tac toe menu')
def text(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',90)
    msgobj=fontobj.render(msg,False,green)
    screen.blit(msgobj,(x,y))
def st(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',200)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))


def _text(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',90)
    msgobj=fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))
def  button():
     pygame.draw.rect(screen,green,(100,450, 200,300),10)
     pygame.draw.rect(screen,red,(600,450, 200,300),10)
    
def menu():
   
    while True :
        button()
        text('play',120,580,blue)
        _text('quit',625,580,red)           
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y=event.pos
                if x >100 and x < 300 and y  > 450 and y < 750:
                    st('play',300,200,white)
                    pygame.display.update()
                    screen.fill(black)
                    time.sleep(1)
                    game()
                    x=0
                    y=0
                if x>600 and x<800 and y>450 and y< 750:
                    st('quit',300,200,white)
                    pygame.display.update()
                    quit()
                    

menu()              



    
  
