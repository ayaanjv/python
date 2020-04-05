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
b=[]


for circle in range (1,300,1):
    a=[random.randint(0,820), random.randint (0,640) ]
    b.append(a)

def score(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',100)
    msgobj=fontobj.render(msg,False,blue)
    screen.blit(msgobj,(x,y))
def insrtuctions(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',35)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))                
def game():
    global x
    global y
    global xchange
    global ychange
    global red_pad
    global blue_pad
    global blue_pad_up
    global red_pad_up
    global change
    global red_points
    global blue_points
    global screen
    x=410
    y=320
    xchange=5
    ychange=5
    red_pad=200
    blue_pad=200
    blue_pad_up=0
    red_pad_up=0
    change=1
    red_points=0
    blue_points=0
    screen = pygame.display.set_mode((820,640))
    game_start= True
    while game_start:
        pygame.display.update()
        for snowflake in b:
            pygame.draw.circle(screen,white,snowflake, 1)
        insrtuctions('Use up and down keys to make blue paddle move up and down',0,10,yellow)
        insrtuctions("First one to five wins ",0,210,yellow)
        insrtuctions('(Press Space Bar to continue)',0,410,yellow)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_SPACE:
                    game_start = False
                    break
    while True:
        pygame.display.update()
        screen.fill(black)

        for snowflake in b:
            pygame.draw.circle(screen,white,snowflake, 1)

        speed=random.randint(10,15)
        direction=random.choice([-speed,speed])

        redP=pygame.draw.rect(screen,red,(0,red_pad,30,150))
        blueP=pygame.draw.rect(screen,blue,(790,blue_pad,30,150))
        Ball=pygame.draw.circle(screen,lime,(x,y),30)

        score(str(blue_points),710,-10,white)
        score(str(red_points),55,-10,white)

        x=x+xchange
        y=y+ychange

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
            blue_pad=blue_pad+7
        if blue_pad_up==1:
            blue_pad=blue_pad-7



        
        if blue_pad <=0:
            blue_pad=0
        if blue_pad >=490:
            blue_pad=490        

        if red_pad <=0:
            red_pad=0
        if red_pad >=490:
            red_pad=490
                  
        if y<=50:
            ychange=speed
            ychange=+ychange
        if y>=590:
            ychange=speed
            ychange=-ychange
        if x<400:
            if  red_pad>y:
                red_pad=red_pad-10
            elif  red_pad<y:
                red_pad=red_pad+10
           
        elif x>320:
            if red_pad!=200:
                if  red_pad<200:
                    red_pad=red_pad+5
                elif  red_pad>200:
                    red_pad=red_pad-5
   
        if blueP.colliderect(Ball):
          xchange=speed
          xchange=-xchange
          ychange=direction
          
        if redP.colliderect(Ball):
          xchange=speed
          xchange=+xchange
          ychange=direction
     
        if x<=-30:
           x=850
           y=320
           red_pad=200
           blue_pad=200
           time.sleep(.5)
           blue_points=blue_points+change
           score(str(blue_points),55,-10,white)
           speed=5
           time.sleep(1)
        if x>=850:
            x=100
            y=320
            red_pad=200
            blue_pad=200
            time.sleep(.5)
            red_points=red_points+change
            score(str(red_points),710,-10,white)
            speed=5
            time.sleep(1)

        if blue_points==5:
            screen.fill(black)
            for snowflake in b:
                pygame.draw.circle(screen,white,snowflake, 1)
            score(str(blue_points),710,-10,white)
            score(str(red_points),55,-10,white)
            pygame.draw.rect(screen,red,(0,red_pad,60,230))
            pygame.draw.rect(screen,blue,(760,blue_pad,60,230))
            pygame.display.update()
            time.sleep(.5)
            screen.fill(black)
            score('BLUE WON',145,250,blue)
            pygame.display.update()
            time.sleep(2)
            screen.fill(black)
            screen = pygame.display.set_mode((900,900))
            break
        if red_points==5:
            screen.fill(black)
            for snowflake in b:
                pygame.draw.circle(screen,white,snowflake, 1)
            score(str(red_points),55,-10,white)
            score(str(blue_points),710,-10,white)
            pygame.draw.rect(screen,red,(0,red_pad,60,230))
            pygame.draw.rect(screen,blue,(760,blue_pad,60,230))
            pygame.display.update()
            time.sleep(2)
            screen.fill(black)
            score('RED WON', 175, 250,red)
            pygame.display.update()
            time.sleep(2)
            screen.fill(black)
            screen = pygame.display.set_mode((900,900))
            break


game()
