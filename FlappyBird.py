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
orange = (255,128,0)
purple = (128, 0, 128)
silver = (192, 192, 192)
teal = (0, 128, 128)
yellow = (255, 255, 0)
sky = (102,255,255)
x=410
y=320
move=0
fly=1
flap=1
fall=2
Bx=800
Bx2=1100
Bx3=1400
pipe_y=0
pipe_y2=640
pipe_y3=0
pipe_y4=640
pipe_y5=0
pipe_y6=640
topY=300
topY2=100
topY3=200
point=0
life=3
color=orange
rainbow=[red,orange,yellow,green,blue,purple]
hi=0
fast=-1

def insrtuctions(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',30)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))                
def score(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',50)
    msgobj=fontobj.render(msg,False,blue)
    screen.blit(msgobj,(x,y))                
def X(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',100)
    msgobj=fontobj.render(msg,False,blue)
    screen.blit(msgobj,(x,y))              
def Flappy():
    global screen
    global x
    global y
    global move
    global fly
    global flap
    global fall
    global Bx
    global Bx2
    global Bx3
    global pipe_y
    global pipe_y2
    global pipe_y3
    global pipe_y4
    global pipe_y5
    global pipe_y6
    global topY
    global topY2
    global topY3
    global point
    global life
    global colors
    global rainbow
    global hi
    global fast
    game_start= True
    while game_start:
        fpsclock.tick(25)
        pygame.display.update()
        screen.fill(sky)
        insrtuctions('Use space bar to make bird fly',10,10,white)
        insrtuctions('Use R key to change color of bird',10,110,white)
        insrtuctions("Don't touch the top,bottom,or pipes to stay alive",10,210,white)
        insrtuctions('(Press Space Bar to continue)',10,310,white)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_SPACE:
                    game_start = False
                    break
    while True:
        pygame.display.update()
        screen.fill(sky)
        
        bird=pygame.draw.circle(screen,yellow,(x,y),40)
        pygame.draw.circle(screen,yellow,(680,70),30)
        pygame.draw.circle(screen,yellow,(600,70),30)
        pygame.draw.circle(screen,yellow,(520,70),30)
        Bx-=fly
        Bx2-=fly
        Bx3-=fly
        r=random.choice(rainbow)
    

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()        
                exit()
            elif event.type == KEYDOWN:
                if event.key==K_SPACE:
                    move=1
                if event.key==K_r: 
                    color=r
            elif event.type == KEYUP:   
                if event.key==K_SPACE:
                    move=0
        
    #1
        topPipe = pygame.draw.rect(screen,green,(Bx,0,70,topY))
        botPipe = pygame.draw.rect(screen,green,(Bx,topY+200,70,600))
    #2
        topPipe2 = pygame.draw.rect(screen,green,(Bx2,0,70,topY2))
        botPipe2= pygame.draw.rect(screen,green,(Bx2,topY2+200,70,600))  
    #3
        topPipe3 = pygame.draw.rect(screen,green,(Bx3,0,70,topY3))
        botPipe3 = pygame.draw.rect(screen,green,(Bx3,topY3+200,70,600))
        

        if Bx==820:
           if topY == topY2:
                topY2 = random.randint(1,4)*100

        
        if move==1:
            y=y-flap
        if move==0:
            y=y+fall
            
        if y-27<=0: 
            time.sleep(1)
            y=320
            Bx=800
            Bx2=1100
            Bx3=1400
            life=life-1
            point=0
            time.sleep(1)
            size = random.randint(1,5)
        if y+27>= 640:
            time.sleep(1)
            y=320
            Bx=800
            Bx2=1100
            Bx3=1400
            life=life-1 
            point=0
            time.sleep(1)
            size = random.randint(1,5)   
        if Bx<=-90:
            Bx=820
            
        if Bx2<=-90:
            Bx2=820
        if Bx3<=-90:
            Bx3=820
            
       
       
        if bird.colliderect(topPipe) or bird.colliderect(botPipe):
            time.sleep(1)
            y=320
            Bx=800
            Bx2=1100
            Bx3=1400
            life=life-1
            point=0
            time.sleep(1)
            size = random.randint(1,5)
        if bird.colliderect(topPipe2) or bird.colliderect(botPipe2):
            time.sleep(1)
            y=320
            Bx=800
            Bx2=1100
            Bx3=1400
            point=0
            life=life-1
            time.sleep(1)
            size = random.randint(1,5)
        if bird.colliderect(topPipe3) or bird.colliderect(botPipe3):
            time.sleep(1)
            y=320
            Bx=800
            Bx2=1100
            Bx3=1400
            life=life-1
            point=0
            time.sleep(1)
            size = random.randint(1,5)
            
       
        if life == 2:
            pygame.draw.circle(screen,black,(520,70),30)
            X('X',490,20,red)
        if life == 1:
            pygame.draw.circle(screen,black,(520,70),30)
            X('X',490,20,red)
            pygame.draw.circle(screen,black,(600,70),30)
            X('X',570,20,red)
        if life == 0:
            pygame.draw.circle(screen,black,(520,70),30)
            X('X',490,20,red)
            pygame.draw.circle(screen,black,(600,70),30)
            X('X',570,20,red)
            pygame.draw.circle(screen,black,(680,70),30)
            X('X',650,20,red)
            pygame.display.update()
            time.sleep(2)
            screen.fill(sky)
            screen = pygame.display.set_mode((900,900))
            life=3
            break
            
        
             
        if Bx == 320:
            point=point+1
            score(str(point),770,-10,blue)
            fast=fast+1
        if Bx2 == 320:
            point=point+1
            score(str(point),770,-10,blue)
            fast=fast+1
        if Bx3 == 320:
            point=point+1
            fast=fast+1
            score(str(point),770,-10,blue)
        score('Your Score:',500,-10,blue)            
        score(str(point),770,-10,blue)
        if point>hi:
            hi=point
##            game_end=True      
            with open('High_Score','w') as file:
                file.write(str(point))
        score('High Score:',100,-10,blue)
        score(str(hi),370,-10,blue)
        
        pygame.display.update

        with open ("High_Score",'r') as file:
            for l in file:
                hi=l.strip()
                hi=int(hi)
        print(fast)
        if fast==10:
            fly=fly+1
            flap=flap+1
            fall=fall+1
            fast=0
        if point==10:
            fly=2
            flap=2
            fall=3
            fast=0
        if point==0:
            fly=1
            flap=1
            fall=2
            fast=-1
   
