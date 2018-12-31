from pygame.locals import*
import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((820,640))
pygame.display.set_caption ('Flappybird')
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
purple = (128, 0, 128)
silver = (192, 192, 192)
teal = (0, 128, 128)
yellow = (255, 255, 0)
sky = (102,255,255)
x=410
y=320
move=0
fly=1
brick=800
brick_two=1100
brick_three=1400
flap=1
ran=random.randint(100,450)
dom=random.randint(100,450)
dint=random.randint(100,450)
                 
while True:    
    pygame.display.update()
    screen.fill(sky)
    pygame.draw.rect(screen,green,(brick,0,80,640))
    pygame.draw.rect(screen,sky,(brick,ran,80,150))
    pygame.draw.rect(screen,green,(brick_two,0,80,640))
    pygame.draw.rect(screen,sky,(brick_two,dom,80,150))
    pygame.draw.rect(screen,green,(brick_three,0,80,640))
    pygame.draw.rect(screen,sky,(brick_three,dint,80,150))
    pygame.draw.circle(screen,yellow,(x,y),40)
    brick=brick-fly
    brick_two=brick_two-fly
    brick_three=brick_three-fly
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_SPACE:
                move=1
        if event.type == KEYUP:
            if event.key==K_SPACE:
                move=0
    if move==1:
        y=y-flap
    if move==0:
        y=y+flap
        
    if y-40<=-2:
        time.sleep(1)
        y=320
        brick=700
        brick_two=1000
        brick_three=1300
        time.sleep(1)
        ran=random.randint(100,400)
        dom=random.randint(100,400)
    if y+40 >= 642:
        time.sleep(1)
        y=320
        brick=700
        brick_two=1000
        brick_three=1300
        time.sleep(1)
        ran=random.randint(100,400)
        dom=random.randint(100,400)
        
    if brick==-80:
        brick=820
        ran=random.randint(100,400)
    if brick_two==-80:
        brick_two=820
        dom=random.randint(100,400)
    if brick_three==-80:
        brick_three=820
        dint=random.randint(100,450)
