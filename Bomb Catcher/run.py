import sys, random, time, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Bomb Catcher")

blue = (17, 238, 238, 0)
red = (245, 112, 112, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:  # ESC
                sys.exit()


    screen.fill((0, 0, 200))
    pygame.draw.rect(screen, blue, (10, 10, 30, 100), 0)
    pygame.draw.circle(screen, red, (19, 19), 10, 0)
    pygame.display.flip()
