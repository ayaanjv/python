from pygame.locals import*
import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((640,480))
<<<<<<< HEAD
pygame.display.set_caption ('PONG')
=======
pygame.display.set_caption ('G')
>>>>>>> 20c06d5ed2f1f34e8c3843fa9f9ed4d2dd69db2b
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
while True:
    pygame.draw.circle(screen,white,(300,440,), 50)
    
