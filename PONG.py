import pygame
import random
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((820,640))
pygame.display.set_caption('PONG')
pygame.display.update()
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
x=320
y=240
xchange=1
ychange=1
while True:
    speed=random.randint(0,2)
    pygame.display.update()
    screen.fill(black)
    pygame.draw.rect(screen,red,(0,170,60,230))
    pygame.draw.rect(screen,blue,(760,170,60,230))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(screen,lime,(x,y),50)
    x=x+xchange
    y=y+ychange
    if x>=770:
        xchange=speed
        xchange=-xchange
    if x<=50:
        xchange=speed
        xchange=+xchange
    if y<=50:
        ychange=speed
        ychange=+ychange
    if y>=590:
        ychange=speed
        ychange=-ychange
