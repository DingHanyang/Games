import pygame
import sys
from pygame.locals import *

import Snake.constant
from Snake.food import Food
from Snake.prop import Prop
from Snake.snake import Snake


class SnakeGame(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")

        self.screen = pygame.display.set_mode((800, 600))

        # game elements object
        self.snake = Snake()
        self.food = Food()
        self.prop = Prop()

        # map
        self.map = []

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

    def draw_map(self):
        """
        draw game map
        """

    def run(self):
        while True:
            self.event_manager()
            self.screen.fill((0, 0, 200))
            pygame.display.update()


game = SnakeGame()
game.run()
