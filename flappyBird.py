from pygame.locals import*
import pygame
import random
import time
fpsclock=pygame.time.Clock()
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
fly=3
brick=800
brick2=1100
brick3=1400
flap=5
fall=6
points=0
Big=random.randint(1,5)
tall=random.randint(1,5)
size = random.randint(1,5)

gap=0
##def score(msg,x,y,blue):
##    fontobj=pygame.font.SysFont('freesans',100)
##    msgobj=fontobj.render(msg,False,blue)
##    screen.blit(msgobj,(x,y))                
def image():
    img=pygame.image.load('flappy1.png')
    screen.blit(img,(x,y))
def Block():#1
    img=pygame.image.load('pipe1.png')
    screen.blit(img,(brick,-200))
    img=pygame.image.load('pipe2.png')
    screen.blit(img,(brick,370))
def block():#2
    img=pygame.image.load('pipe1.png')
    screen.blit(img,(brick2,-200))
    img=pygame.image.load('pipe2.png')
    screen.blit(img,(brick2,370))
def BLOCK():#3
    img=pygame.image.load('pipe1.png')
    screen.blit(img,(brick3,-200))
    img=pygame.image.load('pipe2.png')
    screen.blit(img,(brick3,370))
    

while True:    
    pygame.display.update()
    fpsclock.tick(50)
    screen.fill(sky)

##    if size == 1:
##        top_pipe=-800
##        bot_pipe=1000
##        gap=80             
##        Block()
##    if size == 2:
##        top_pipe=-800
##        bot_pipe=1000
##        gap=160
##        Block()
##    if size == 3:
##        top_pipe=-800
##        bot_pipe=1000
##        gap=240
##        Block()
##    if size == 4:
##        top_pipe=-800
##        bot_pipe=1000
##        Block()
##    if size == 5:
##        top_pipe=-800
##        bot_pipe=1000       
##        Block()
##
##    if Big == 1:
##        top_pipe2=80
##        bot_pipe2=-400
##        block()
##    if Big == 2:
##        top_pipe2=160
##        bot_pipe2=-320
##        block()
##    if Big == 3:
##        top_pipe2=240
##        bot_pipe2=-240
##        block()
##    if Big == 4:
##        top_pipe2=320
##        bot_pipe2=-160
##        block()
##    if Big == 5:
##        top_pipe2=400
##        bot_pipe2=-80
##        block()
##
##    if tall == 1:
##        top_pipe3=80
##        bot_pipe3=-400
##        BLOCK()
##    if tall == 2:
##        top_pipe3=160
##        bot_pipe3=-320
##        BLOCK()
##    if tall == 3:
##        top_pipe3=240
##        bot_pipe3=-240
##        BLOCK()
##    if tall == 4:
##        top_pipe3=320
##        bot_pipe3=-160
##        BLOCK()
##    if tall == 5:
##        top_pipe3=400
##        bot_pipe3=-80
##        BLOCK()
##
    Block()
    BLOCK()
    block()
    image()
##    score(str(points),710,-10,yellow)
    brick=brick-fly
    brick2=brick2-fly
    brick3=brick3-fly

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
        y=y+fall
        
    if y+9<=0:
        time.sleep(1)
        y=320
        brick=800
        brick2=1100
        brick3=1400
        points=0
        time.sleep(1)
        size = random.randint(1,5)
    if y+56 >= 640:
        time.sleep(1)
        y=320
        brick=800
        brick2=1100
        brick3=1400
        points=0
        time.sleep(1)
        size = random.randint(1,5)
##    print (brick)   
    if brick<=-90:
        brick=800
        size = random.randint(1,5)
    if brick2<=-90:
        brick2=820
        Big=random.randint(1,5)
    if brick3<=-90:
        brick3=820
        tall=random.randint(1,5)



