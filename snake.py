from pygame.locals import*
import pygame
import random
import time
fpsclock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((820,640))
pygame.display.set_caption ('snake')
red = (255,0,0)
green = (0,204,0)
blue = (0,0,255)
orange = (204,103,0)
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

a=random.randint(0,770)
b=random.randint(0,690)
x=100
y=100
up=0
down=0
left=0
right=0
snake_up=0
body=25
point=0
keep=0

def score(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',100)
    msgobj=fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))                

snake=[[x,y]]

while True:
    fpsclock.tick(25)
    pygame.display.update()
    screen.fill(olive)
    SNAKE=pygame.draw.rect(screen,orange,(x,y,25,25))
    MOUSE=pygame.draw.rect(screen,silver,(a,b,25,25))

    for s in snake:
        pygame.draw.rect(screen,orange,(s[0],s[1],25,25))
    snake.insert(0,(x,y))
    snake.pop()
   
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                snake_up=1
            elif event.key==K_DOWN:
                snake_up=2
            if event.key==K_RIGHT:
                snake_up=3
            elif event.key==K_LEFT:
                snake_up=4


    if snake_up==1:#up
        if down == 10:
            keep=1
        up=10
        down=0
        left=0
        right=0
        if keep==1:
            keep=0
            up=0
            down=10
            snake_up=2
        y=y-up
    if snake_up==2:#down
        if up == 10:
            keep=1
        up=0
        down=10
        left=0
        right=0
        if keep==1:
            keep=0
            up=10
            down=0
            snake_up=1
        y=y+down
    if snake_up==3:#right
        if left == 10:
            keep=1
        up=0
        down=0
        left=0
        right=10
        if keep==1:
            keep=0
            right=0
            left=10
            snake_up=4
        x=x+right
    if snake_up==4:#left
        if right==10:
            keep=1
        up=0
        down=0
        left=10
        right=0
        if keep==1:
            keep=0
            left=0
            right=10
            snake_up=3    
        x=x-left
                
    if y<=0:
        screen.fill(olive)
        pygame.draw.rect(screen,orange,(x,y,25,25))
        pygame.draw.rect(screen,silver,(a,b,25,25))
        x=100
        y=100
        up=0
        down=0
        left=0
        right=0
        snake_up=0
        body=25
        point=0
        snake=[]
    if y>=640:
        screen.fill(olive)
        pygame.draw.rect(screen,orange,(x,y,25,25))
        pygame.draw.rect(screen,silver,(a,b,25,25))
        x=100
        y=100
        up=0
        down=0
        left=0
        right=0
        snake_up=0
        body=25
        point=0
        snake=[]
    if x<=0:
        screen.fill(olive)
        pygame.draw.rect(screen,orange,(x,y,25,25))
        pygame.draw.rect(screen,silver,(a,b,25,25))
        x=100
        y=100
        up=0
        down=0
        left=0
        right=0
        snake_up=0
        body=25
        point=0
        snake=[]
    if x>=820:
        screen.fill(olive)
        pygame.draw.rect(screen,orange,(x,y,25,25))
        pygame.draw.rect(screen,silver,(a,b,25,25))
        x=100
        y=100
        up=0
        down=0
        left=0
        right=0
        snake_up=0
        body=25
        point=0
        snake=[]
    if SNAKE.colliderect(MOUSE):
        a=random.randint(0,820)
        b=random.randint(0,640)
        body=body+25
        point=point+1
        snake.insert(0,(x,y))
                
    score(str(point),710,-10,blue)
    pygame.display.update
