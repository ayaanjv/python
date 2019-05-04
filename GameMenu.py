from Pong import*
from TicTacToe import*
from FlappyBird import*
from Snake import*
import pygame
import time
import GameMenu
from pygame.locals import*
pygame.init()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (204,103,0)
white  = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption ('Pong Menu')
def st(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',70)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))
def text(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',150)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))

def button():
    pygame.draw.rect(screen,green,(0,450, 290,450),10)
    pygame.draw.rect(screen,red,(600,0,295,900),10)
    pygame.draw.rect(screen,blue,(300,450,290,450),10)
    pygame.draw.rect(screen,yellow,(0,0,290,445),10)
    pygame.draw.rect(screen,orange,(300,0,290,445),10)
   
while True :
##     screen.fill(white)
     button()
     st('Tic',85,570,green)
     st('Tac',85,640,green)
     st('Toe',85,710,green)
     st('Quit',675,400,red)
     st('Pong',365,620,blue)
     st('Flappy',40,120,yellow)
     st('Bird',70,190,yellow)
     st('Snake',350,160,orange)
     pygame.display.update()
     for event in pygame.event.get():
         if event.type==QUIT:
             pygame.quit()
             exit()
         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
             x,y=event.pos
             if x >300 and x < 600 and y  > 450 and y < 900:
                 screen.fill(black)   
                 text('Pong',300,300,blue)
                 pygame.display.update()
                 screen.fill(black)
                 time.sleep(1)
                 game()
                 x=0
                 y=0
             if x >0 and x < 300 and y  > 0 and y < 450:
                 screen.fill(black)   
                 text('Flappy Bird',100,300,yellow)
                 pygame.display.update()
                 screen.fill(black)
                 time.sleep(1)
                 screen = pygame.display.set_mode((820,640))
                 Flappy()
                 x=0
                 y=0
             if x >300 and x < 600 and y  > 0 and y < 450:
                 screen.fill(black)   
                 text('Snake',250,300,orange)
                 pygame.display.update()
                 screen.fill(black)
                 time.sleep(1)
                 screen = pygame.display.set_mode((820,640))
                 Snake()
                 x=0
                 y=0
             if x >0 and x < 300 and y  > 450 and y < 900:
                 screen.fill(black)   
                 text('Tic Tac Toe',70,300,green)
                 pygame.display.update()
                 screen.fill(black)
                 time.sleep(1)
                 TTT()
                 x=0
                 y=0
           
             if x >600 and x<900 and y>0 and y< 900:
                 screen.fill(black)   
                 text('Quit',300,300,red)
                 pygame.display.update()
                 quit()

