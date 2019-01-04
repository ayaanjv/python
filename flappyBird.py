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
points=0 
size = random.randint(1,5)
top_pipe=80
bot_pipe=-80


def score(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',100)
    msgobj=fontobj.render(msg,False,blue)
    screen.blit(msgobj,(x,y))                
def Block():#1
    pygame.draw.rect(screen,green,(brick,0,80,top_pipe))
    pygame.draw.rect(screen,green,(brick,640,80,bot_pipe))
##def block():#2
    
while True:    
    pygame.display.update()
    screen.fill(sky)

    if size == 1:
        top_pipe=80
        bot_pipe=-400
        Block()
    if size == 2:
        top_pipe=160
        bot_pipe=-320
        Block()
    if size == 3:
        top_pipe=240
        bot_pipe=-240
        Block()
    if size == 4:
        top_pipe=320
        bot_pipe=-160
        Block()
    if size == 5:
        top_pipe=400
        bot_pipe=-80
        Block()
    pygame.draw.circle(screen,yellow,(x,y),40)

    score(str(points),710,-10,yellow)
    brick=brick-fly
    
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key==K_SPACE:
                move=1
        elif event.type == KEYUP:
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
        points=0
        time.sleep(1)
        size = random.randint(1,2)
    if y+40 >= 642:
        time.sleep(1)
        y=320
        brick=700
        brick_two=1000
        brick_three=1300
        points=0
        time.sleep(1)
        size = random.randint(1,2)
        
    if brick==-80:
        brick=820
        size = random.randint(1,2)
##    if brick_two==-80:
##        brick_two=820
##        gap_two=820
##        dom=random.randint(100,400)
##    if brick_three==-80:
##        brick_three=820
##        gap_three=820
##        dint=random.randint(100,450)

    
