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
orange = (255,128,0)
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
speed=7
a=random.randint(0,770)
b=random.randint(0,590)
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
snake=[[x,y]]
color=orange
rainbow=[red,orange,yellow,green,blue,purple]
hi=0
game_end= False
name=[]

def score(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',50)
    msgobj=fontobj.render(msg,False,orange)
    screen.blit(msgobj,(x,y))
def insrtuctions(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',30)
    msgobj=fontobj.render(msg,False,white)
    screen.blit(msgobj,(x,y))                


def Snake():
    global a
    global b
    global x
    global y
    global up
    global down
    global left
    global right
    global snake_up
    global body
    global point
    global keep
    global snake
    global screen
    global color
    global rainbow
    global hi
    global game_end
    global name
    game_start= True
    while game_start:
        fpsclock.tick(25)
        pygame.display.update()
        screen.fill(olive)
        insrtuctions('Use Up,Down,Left,Right keys to move snake and eat mouse',10,10,white)
        insrtuctions('Use R key to change color of snake',10,110,white)
        insrtuctions("Don't touch the border or you wil die",10,210,white)
        insrtuctions('(Press Space Bar to continue)',10,310,white)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_SPACE:
                    game_start = False
                    break
            
    while True:
        fpsclock.tick(25)
        pygame.display.update()
        screen.fill(olive)
        
        SNAKE=pygame.draw.rect(screen,color,(x,y,25,25))
        MOUSE=pygame.draw.rect(screen,silver,(a,b,25,25))
        r=random.choice(rainbow)
    
        for s in snake:
            pygame.draw.rect(screen,color,(s[0],s[1],25,25))
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
                if event.key==K_r:
                    color=r
                    

        if snake_up==1:#up
            if down == speed:
                keep=1
            up=speed
            down=0
            left=0
            right=0
            if keep==1:
                keep=0
                up=0
                down=speed
                snake_up=2
            y=y-up
        if snake_up==2:#down
            if up == speed:
                keep=1
            up=0
            down=speed
            left=0
            right=0
            if keep==1:
                keep=0
                up=speed
                down=0
                snake_up=1
            y=y+down
        if snake_up==3:#right
            if left == speed:
                keep=1
            up=0
            down=0
            left=0
            right=speed
            if keep==1:
                keep=0
                right=0
                left=speed
                snake_up=4
            x=x+right
        if snake_up==4:#left
            if right==speed:
                keep=1
            up=0
            down=0
            left=speed
            right=0
            if keep==1:
                keep=0
                left=0
                right=speed
                snake_up=3    
            x=x-left
                    
        if y<=-30:


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
            time.sleep(1)
            screen.fill(green)
            screen = pygame.display.set_mode((900,900))
            break
        if y>=660:
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
            time.sleep(1)
            screen.fill(green)
            screen = pygame.display.set_mode((900,900))
            break
        if x<=-30:
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
            time.sleep(1)
            screen.fill(green)
            screen = pygame.display.set_mode((900,900))
            break
        if x>=825:
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
            time.sleep(1)
            screen.fill(green)
            screen = pygame.display.set_mode((900,900))
            break
        if SNAKE.colliderect(MOUSE):
            a=random.randint(0,820)
            b=random.randint(0,640)
            body=body+25
            point=point+1
            snake.insert(0,(x,y))
        score('Your Score:',500,-10,blue)            
        score(str(point),770,-10,blue)
##        if point>hi:
##            hi=point
##            game_end=True      
##            with open('HighScore','w') as file:
##                file.write(str(point))
##        score('High Score:',100,-10,blue)
##        score(str(hi),370,-10,red)
##        
        pygame.display.update
##
##        with open ("HighScore",'r') as file:
##            for l in file:
##                hi=l.strip()
##                hi=int(hi)
##
    
    while game_end:
        screen.fill(olive)
        score('Type in your name(up to ten letters)',10,10,white)
        score('(letters only)',10,50,white)
        if len(name)<10:
            n="".join(name)
            score(n,400,90,red)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_a:
                    name.append('a')                        
                elif event.key==K_b:
                    name.append('b')
                elif event.key==K_c:
                    name.append('c')
                elif event.key==K_d:
                    name.append('d')
                elif event.key==K_e:
                    name.append('e')
                elif event.key==K_f:
                    name.append('f')
                elif event.key==K_g:
                    name.append('g')
                elif event.key==K_h:
                    name.append('h')
                elif event.key==K_i:
                    name.append('i') 
                elif event.key==K_j:
                    name.append('j')
                elif event.key==K_k:
                    name.append('k')
                elif event.key==K_l:
                    name.append('l')
                elif event.key==K_m:
                    name.append('m')
                elif event.key==K_n:
                    name.append('n')
                elif event.key==K_o:
                    name.append('o')
                elif event.key==K_p:
                    name.append('p')
                elif event.key==K_q:
                    name.append('q')
                elif event.key==K_r:
                    name.append('r')
                elif event.key==K_s:
                    name.append('s')
                elif event.key==K_t:
                    name.append('t')
                elif event.key==K_u:
                    name.append('u')
                elif event.key==K_v:
                    name.append('v')
                elif event.key==K_w:
                    name.append('w')
                elif event.key==K_x:
                    name.append('x')
                elif event.key==K_y:
                    name.append('y')
                elif event.key==K_z:
                    name.append('z')
        
               
                
                elif event.key==K_DELETE:
                    l=len(name)
                    l=l-1
                    name.pop(l)
                elif event.key==K_BACKSPACE:
                    l=len(name)
                    l=l-1
                    name.pop(l)
                elif event.key==K_RETURN:
                    with open('leader','w') as file:
                        file.write(n)
                        name=''
                        game_end = False
                        screen.fill(black)
                        break              
Snake()
