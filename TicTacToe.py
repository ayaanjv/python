import pygame
import random
import time
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption ('TIC TAC TOE')
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white  = (255,255,255)
black = (0,0,0)
count = 0




def board():
    pygame.draw.line(screen, white, (0,300),(900,300),10)
    pygame.draw.line(screen, white, (0,600),(900,600),10)
    pygame.draw.line(screen, white, (300,0),(300,900),10)
    pygame.draw.line(screen, white, (600,0),(600,900),10)
    winner()
    pygame.display.update()

def drawX(x,y):
    pygame.draw.line(screen, red, (x,y),(x+300,y+300),10)
    pygame.draw.line(screen,red,(x+300,y),(x,y+300),10)
def drawO(x,y):
    pygame.draw.circle(screen,green,(x + 150, y + 150),150,10)

def show_text(msg,x,y,blue):
    fontobj=pygame.font.SysFont('freesans',150)
    msgobj=fontobj.render(msg,False,blue)
    screen.blit(msgobj,(x,y))

def winner():
    if TIC[1]==TIC[2]==TIC[3]=='x'or TIC[1]==TIC[4]==TIC[7]=='x'or TIC[4]==TIC[5]==TIC[6]=='x' or TIC[1]==TIC[5]==TIC[9]=='x'or TIC[3]==TIC[5]==TIC[7]=='x' or TIC[3]==TIC[6]==TIC[9]=='x' or TIC[1]==TIC[4]==TIC[7]=='x'or TIC[2]==TIC[5]==TIC[8]=='x':
        time.sleep(1)
        screen.fill((black))
        show_text('X WINS',200,350,red)
        pygame.display.update()
        time.sleep(1.5)
        screen.fill(black)
        return 1
        
    elif TIC[1]==TIC[2]==TIC[3]=='o'or TIC[1]==TIC[4]==TIC[7]=='o'or TIC[4]==TIC[5]==TIC[6]=='o' or TIC[1]==TIC[5]==TIC[9]=='o'or TIC[3]==TIC[5]==TIC[7]=='o' or TIC[3]==TIC[6]==TIC[9]=='o' or TIC[1]==TIC[4]==TIC[7]=='o'or TIC[2]==TIC[5]==TIC[8]=='o':
        time.sleep(1)
        screen.fill((black))
        show_text('O WINS',200,350,green)
        pygame.display.update()
        time.sleep(1.5)
        screen.fill(black)
        return 1
        
    elif '' not in TIC.values():
        time.sleep(1)
        screen.fill((black))
        show_text('TIE',330,350,blue)
        pygame.display.update()
        time.sleep(1.5)
        screen.fill(black)
        return 1
    
    return 0
    
def game():
    global flag
    global TIC
    global points
    TIC ={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
    flag = False
    points=[]
    
    while True:
        pygame.display.update()
        if winner()==1:
            return
        
        board()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:
                x,y=event.pos
                ax = ((x//300)*300)
                by = ((y//300)*300)
                index=int((ax+by*3)/300)+1
               
                
                if(not([ax,by] in points)):
                    if flag == False:
                        drawX(ax,by)
                        TIC[index]='x'
                        flag = True
                    elif flag== True:
                        drawO(ax,by)
                        TIC[index]='o'
                        flag=False

                points.append([ax,by])
                
                if  not([ax,by] in points) :
                    points.append [ax,by]
