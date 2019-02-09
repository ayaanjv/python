from pygame.locals import*
import pygame
import random
import time
fpsclock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((900,640))
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
brick=900
brick2=1200
brick3=1500
flap=3
fall=4
points=0
gap=880
top_pipe=240
bot_pipe=-240
top_pipe2=240
bot_pipe2=-240
top_pipe3=240
bot_pipe3=-240
Big=random.randint(1,5)
tall=random.randint(1,5)
size = random.randint(1,5)
pipe_y=0
pipe_y2=640

gap=0
##def score(msg,x,y,blue):
##    fontobj=pygame.font.SysFont('freesans',100)
##    msgobj=fontobj.render(msg,False,blue)
##    screen.blit(msgobj,(x,y))                
def image():
    img=pygame.image.load('flappy1.png')
    screen.blit(img,(x,y))
def Block():#1
    pygame.draw.rect(screen,green,(brick,pipe_y,80,top_pipe))
    pygame.draw.rect(screen,green,(brick,pipe_y2,80,bot_pipe))
    
def block():#2
    pygame.draw.rect(screen,green,(brick2,0,80,top_pipe2))
    pygame.draw.rect(screen,green,(brick2,640,80,bot_pipe2))
    
def BLOCK():#3
    pygame.draw.rect(screen,green,(brick3,0,80,top_pipe3))
    pygame.draw.rect(screen,green,(brick3,640,80,bot_pipe3))

while True:    
    pygame.display.update()
    fpsclock.tick(50)
    screen.fill(sky)
##    if size == Big:
##        Big = random.randint(1,5)
##    if Big == tall:
##        tall = random.randint(1,5)
##    if tall == size:
##        size = random.randint(1,5)
    
    if size == 1:
        top_pipe=80
        bot_pipe=-400
        gap=80             
        Block()
               

    if size == 2:
        top_pipe=160
        bot_pipe=-320
        gap=160
        Block()
    if size == 3:
        top_pipe=240
        bot_pipe=-240
        gap=240
        Block()
    if size == 4:
        top_pipe=320
        bot_pipe=-160
        gap=320
        Block()
    if size == 5:
        top_pipe=400
        bot_pipe=-80
        gap=400
        Block()

    if Big == 1:
        top_pipe2=80
        bot_pipe2=-400
        block()
    if Big == 2:
        top_pipe2=160
        bot_pipe2=-320
        block()
    if Big == 3:
        top_pipe2=240
        bot_pipe2=-240
        block()
    if Big == 4:
        top_pipe2=320
        bot_pipe2=-160
        block()
    if Big == 5:
        top_pipe2=400
        bot_pipe2=-80
        block()

    if tall == 1:
        top_pipe3=80
        bot_pipe3=-400
        BLOCK()
    if tall == 2:
        top_pipe3=160
        bot_pipe3=-320
        BLOCK()
    if tall == 3:
        top_pipe3=240
        bot_pipe3=-240
        BLOCK()
    if tall == 4:
        top_pipe3=320
        bot_pipe3=-160
        BLOCK()
    if tall == 5:
        top_pipe3=400
        bot_pipe3=-80
        BLOCK()

    Block()
    block()
    BLOCK()
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
        
    if y+10<=0: 
        time.sleep(1)
        y=320
        brick=800
        brick2=1100
        brick3=1400
        points=0
        time.sleep(1)
        size = random.randint(1,5)
    if y+60 >= 640:
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
        brick=900
        size = random.randint(1,5)
    if brick2<=-90:
        brick2=900
        Big=random.randint(1,5)
    if brick3<=-90:
        brick3=900
        tall=random.randint(1,5)

    if brick-95 <= x <= brick-15 and y in range(pipe_y,pipe_y+top_pipe) or brick-95 <= x <= brick-15 and y in range(pipe_y2+bot_pipe,pipe_y2):
        time.sleep(1)
        y=320

        brick=800
        brick2=1100
        brick3=1400
        points=0
        time.sleep(1)
        size = random.randint(1,5)



