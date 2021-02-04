from pygame.locals import*
import pygame
import random
import time
import string
fpsclock=pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((975,750))
pygame.display.set_caption ('')
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
people=[]
rNought=9
numPeople=36
Game_Start=0
Game=0
Instruction=1
death=0
def text(msg,x,y,size):
    fontobj=pygame.font.SysFont('Sans',size)
    msgobj=fontobj.render(msg,False,black)
    screen.blit(msgobj,(x,y))
    
class People:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image=pygame.image.load('GreenPerson.png')
        self.image=pygame.transform.rotozoom(self.image,0,0.20)
        self.rect=None
        self.infection=1
        self.color='green'
    def draw(self):
        self.rect=screen.blit(self.image,(self.x,self.y))
    def infect(self):
        self.infection=random.randint(1,10)
        if self.infection<= rNought:
            self.image=pygame.image.load('redPerson.png')
            self.image=pygame.transform.rotozoom(self.image,0,0.20)
            self.color='red'
            
            
class hospital:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image=pygame.image.load('Ambulence.png')
        self.image=pygame.transform.rotozoom(self.image,0,0.048)
        self.rect=None
        self.flag=0
    def draw(self):
        self.move()
        self.rect=screen.blit(self.image,(self.x,self.y))
    def move(self):
        if self.y%2==0:
            if self.flag==1:
                self.x=self.x-75
            elif self.flag==2:
                self.x=self.x+75

        if self.x % 2==0:
            if self.flag==3:
                self.y=self.y-75
            elif self.flag==4:
                self.y=self.y+75
             
        if self.x>=900:
            self.x=870
        elif self.x<=0:
            self.x=45
            
        if self.y>=675:
            self.y=675
        elif self.y<=0:
             self.y=0

ambulence=hospital(55,300)

for peopleX in range(75,925,150):
    for peopleY in range(50,700,150):
        peopleMade=People(peopleX,peopleY)
        people.append(peopleMade)


while Instruction:
    fpsclock.tick(8)
    pygame.display.update()
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                Instruction=0
                Game_Start=1
    text('Rules',400,0,70)
    text('Use arrow keys to move',0,100,50)
    text('Hover over sick people(red) and press Space to cure',0,200,50)
    text("If you aren't able to cure everybody withn 30s, you lose",0,300,50)
    text('If you do you win',0,400,50)
    text('(press Space to Start)',0,500,50)

while Game_Start:
    fpsclock.tick(8)
    pygame.display.update()
    screen.fill(white)

    text('Choose your infection rate',200,100,70)
    text('1,  2,  3,  4,  5,  6,  7,  8,  9',200,200,70)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_1:
               rNought=1
               Game_Start=0
               Game=1
            if event.key==K_2:
               rNought=2
               Game_Start=0
               Game=1
            if event.key==K_3:
               rNought=3
               Game_Start=0
               Game=1
            if event.key==K_4:
               rNought=4
               Game=0
               Game=1
            if event.key==K_5:
               rNought=5
               Game_Start=0
               Game=1
            if event.key==K_6:
               rNought=6
               Game_Start=0
               Game=1
            if event.key==K_7:
               rNought=7
               Game_Start=0
               Game=1
            if event.key==K_8:
               rNought=8
               Game_Start=0
               Game=1
            if event.key==K_9:
               rNought=9
               Game_Start=0
               Game=1
               
for person in people:
    person.infect()
    if person.color=='red':
        numPeople=numPeople-1

clock=pygame.time.Clock()
start_time = pygame.time.get_ticks()
while Game:
    fpsclock.tick(8)
    pygame.display.update()
    screen.fill(white)
    watch  = pygame.time.get_ticks() - start_time
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                ambulence.flag=1
            elif event.key==K_RIGHT:
                ambulence.flag=2
            elif event.key==K_UP:
                ambulence.flag=3
            elif event.key==K_DOWN:
                ambulence.flag=4
            elif event.key==K_SPACE:
                ambulence.flag=5
                
        elif event.type==KEYUP:
            if event.key==K_LEFT:
                ambulence.flag=0
            elif event.key==K_RIGHT:
                ambulence.flag=0
            elif event.key==K_UP:
                ambulence.flag=0
            elif event.key==K_DOWN:
                ambulence.flag=0
            elif event.key==K_SPACE:
                ambulence.flag=0

    
    
    for person in people:
        if  watch/1000>30 and person.color=='red':
            person.image=pygame.image.load('person.png')
            person.image=pygame.transform.rotozoom(person.image,0,0.20)
            person.color='black'
            death=death+1

        person.draw()
        if ambulence.flag==5:
            if ambulence.y%2==0 and ambulence.x % 2>=0:
                if ambulence.y<person.y and  ambulence.y+150>person.y  and ambulence.x<person.x and  ambulence.x+75>person.x:
                    if person.color=='red':
                        person.image=pygame.image.load('bluePerson.png')
                        person.image=pygame.transform.rotozoom(person.image,0,0.20)
                        person.color='blue'
                        numPeople=numPeople+1


    if numPeople==36:
        Game=0

    if watch/1000>=30:
        text('Time left:0',700,0,50)
        Game=0
        

    else:
         text('Time left:'+ str(int(30-watch/1000)),700,0,50)
    ambulence.draw()

while True:
    fpsclock.tick(24)
    pygame.display.update()
    screen.fill(white)
    if numPeople==36:
        text('You Cured Everyone',250,200,70)
    else:
        text('You Failed to Save '+str(36-numPeople)+' People',150,200,70)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
