from StarWars import*
import pygame
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
pygame.display.set_caption ('Pong Menu')
def text(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',150)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))
def st(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',200)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))
def  button():
     pygame.draw.rect(screen,green,(0,300, 300,600),10)
     pygame.draw.rect(screen,red,(595,300, 300,600),10)
    
def pong():
   
    while True :
        button()
        text('Play',20,580,green)
        text('Quit',625,580,red)       
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y=event.pos
                if x >0 and x < 300 and y  > 300 and y < 900:
                    st('Play',300,50,white)
                    pygame.display.update()
                    screen.fill(black)
                    time.sleep(1)
                    game()
                    x=0
                    y=0
                if x>600 and x<900 and y>300 and y< 900:
                    st('Quit',300,50,white)
                    pygame.display.update()
                    quit()


    
  
