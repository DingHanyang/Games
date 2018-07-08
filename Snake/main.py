import pygame
from pygame.locals import *


class SnakeGame(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 500))
