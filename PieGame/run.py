import pygame
import sys
from pygame.locals import *

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((600, 500))
myfont = pygame.font.Font(None, 60)
white = 255, 255, 255
blue = 0, 0, 255
# 第二个参数是抗锯齿
text_image = myfont.render('hello pygame', True, white)

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(text_image, (100, 100))

    # draw a circle
    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)

    pygame.display.update()
