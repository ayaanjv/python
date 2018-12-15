from pygame.locals import*
import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((820,640))
pygame.display.set_caption ('Star Wars')
red = (255,0,0)
green = (0,255,0)
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
purple = (128, 0, 128)
silver = (192, 192, 192)
teal = (0, 128, 128)
yellow = (255, 255, 0)
x=320
y=240
xchange=1
ychange=1
red_pad=200
blue_pad=200
blue_pad_up=0
red_pad_up=0
b=[]
for circle in range (1,300,1):
       a=[random.randint(0,820), random.randint (0,640) ]
       b.append(a)
while True:
    pygame.display.update()
    screen.fill(black)
    for snowflake in b:
        pygame.draw.circle(screen,white,snowflake, 1)
    speed=random.randint(1,4)
    pygame.draw.rect(screen,red,(0,red_pad,60,230))
    pygame.draw.rect(screen,blue,(760,blue_pad,60,230))
    pygame.draw.circle(screen,lime,(x,y),50)
    x=x+xchange
    y=y+ychange
##    print('ball:',x,y,'bpad',blue_pad+100,blue_pad-100)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    if event.type == KEYDOWN:
        if event.key==K_UP:
            blue_pad_up=1
        elif event.key==K_DOWN:
            blue_pad_up=2
        if event.key==K_w:
            red_pad_up=1
        elif event.key==K_s:
            red_pad_up=2

        
    elif event.type==KEYUP:
        if event.key==K_UP:
            blue_pad_up=0
        elif event.key==K_DOWN:
            blue_pad_up=0
        if event.key==K_w:
            red_pad_up=0
        elif event.key==K_s:
            red_pad_up=0

            
    if blue_pad_up==2:
        blue_pad=blue_pad+3
    if blue_pad_up==1:
        blue_pad=blue_pad-3

    if red_pad_up==2:
        red_pad=red_pad+3
    if red_pad_up==1:
        red_pad=red_pad-3

    
    if blue_pad <=0:
        blue_pad=0
    if blue_pad >=410:
        blue_pad=410        

    if red_pad <=0:
        red_pad=0
    if red_pad >=410:
        red_pad=410
        
    if y<=50:
        ychange=speed
        ychange=+ychange
    if y>=590:
        ychange=speed
        ychange=-ychange

    if x == 710 and blue_pad <=y<= blue_pad+200:
      xchange=speed
      xchange=-xchange
      ychange=speed
      ychange=+ychange
    if x == 110 and red_pad <=y<= red_pad+200:
      xchange=speed
      xchange=+xchange
      ychange=speed
      ychange=-ychange
       
