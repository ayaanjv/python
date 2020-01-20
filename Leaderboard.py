from pygame.locals import*
import pygame
import random
import time
fpsclock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((820,640))
pygame.display.set_caption ('Leader')
red = (255,0,0)
green = (0,204,0)
blue = (0,0,255)
white  = (255,255,255)
black = (0,0,0)
aqua = (0,255,255)
fuchsia = (255, 0, 255)
gray = (128, 128, 128)
lime = (0, 255, 0)
maroon = (128, 0, 0)
navyblue = (0, 0, 128)
olive = (128, 128, 0)
orange = (255,128,0)
purple = (128, 0, 128)
silver = (192, 192, 192)
teal = (0, 128, 128)
yellow = (255, 255, 0)
sky = (102,255,255)
fb_hi=0
s_hi=0
fb_name=''
s_name=''

def st(msg,x,y,white):
    fontobj=pygame.font.SysFont('freesans',70)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))
def instructions(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',50)
    msgobj=fontobj.render(msg,False,black)
    screen.blit(msgobj,(x,y))                
def Leader():
    end=True
    global fb_hi
    global s_hi
    global fb_name
    global s_name
    global f
    global s
    global screen
    screen.fill(white)
    pygame.display.update()
    while end:
        with open ("High_Score",'r') as file:
            for l in file:
                fb_hi=l.strip()
                fb_hi=int(fb_hi)
        with open ("HighScore",'r') as file:
            for p in file:
                s_hi=l.strip()
        with open ("Leader",'r') as file:
            for f in file:
                fb_name=f
        with open ("leader",'r') as file:
            for s in file:
                s_name=s

    ##    pygame.display.update()
        instructions('FB Leader:',10,10,black)
        instructions(str(f),250,10,black)
        instructions(str(s),230,70,black)
        instructions('S Leader:',10,70,black)
       
        
        st('Quit',640,300,red)
        pygame.draw.rect(screen,red,(600,0,215,640),10)
        pygame.display.update()
        for event in pygame.event.get():
             if event.type==QUIT:
                 pygame.quit()
                 exit()
             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y=event.pos
                if x >600 and x<820 and y>0 and y< 640:
                     screen.fill(black)   
                     pygame.display.update()
                     screen = pygame.display.set_mode((900,900))
                     end = False
                     break


