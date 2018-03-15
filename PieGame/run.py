import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
white = 255,255,255
blue = 0,0,255
text_image = myfont.render('hellp pygame',True,white)


while 1:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(text_image, (100, 100))
    pygame.display.update()
