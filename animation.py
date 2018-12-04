from pygame.locals import*
import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption ('SNOWFLAKE')
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
b=[]
for circle in range (1,51,1):
        a=[random.randint(0,640), random.randint (0,480) ]
        b.append(a)
 

while True:
    pygame.display.update()
    screen.fill(navyblue)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    for snowflake in b:
        pygame.draw.circle(screen,white,snowflake, 1)
        snowflake[1]=snowflake[1]+1
        if snowflake[1] == 480:
                snowflake[1]=0
    pygame.draw.circle(screen,white,(300,440,), 50) 
    pygame.draw.circle(screen,white,(300,365,), 40)
    pygame.draw.circle(screen,white,(300,300,), 30)
        
     
        
        
