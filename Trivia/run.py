import pygame
import sys

from pygame.locals import *


class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wrong_answer = 0
        self.colors = [color.THECOLORS['white'], color.THECOLORS['white'], color.THECOLORS['white'],
                       color.THECOLORS['white']]

        self.load_data(filename)

    def load_data(self, filename):
        with open(filename, 'r') as f:
            for text_line in f.readlines():
                self.data.append(text_line.strip())
                self.total += 1

    def show_question(self):
        print_text(font1, 210, 5, "TRIVIA GAME")
        print_text(font2, 190, 500 - 20, "Press Keys (1-4) To Answer", color.THECOLORS['purple'])
        print_text(font2, 530, 5, "SCORE", color.THECOLORS['purple'])
        print_text(font2, 550, 25, str(self.score), color.THECOLORS['purple'])

        # get correct answer out of data (first)
        self.correct = int(self.data[self.current + 5])

        # display question
        question = self.current // 6 + 1
        print_text(font1, 5, 80, "QUESTION " + str(question))
        print_text(font2, 20, 120, self.data[self.current], color.THECOLORS['yellow'])

        # respond to correct answer
        if self.scored:
            self.colors = [color.THECOLORS['white'], color.THECOLORS['white'], color.THECOLORS['white'],
                           color.THECOLORS['white']]
            self.colors[self.correct - 1] = color.THECOLORS['green']
            print_text(font1, 230, 380, "CORRECT!", color.THECOLORS['green'])
            print_text(font2, 170, 420, "Press Enter For Next Question", color.THECOLORS['green'])
        elif self.failed:
            self.colors = [color.THECOLORS['white'], color.THECOLORS['white'], color.THECOLORS['white'],
                           color.THECOLORS['white']]
            self.colors[self.wrong_answer - 1] = color.THECOLORS['red']
            self.colors[self.correct - 1] = color.THECOLORS['green']
            print_text(font1, 220, 380, "INCORRECT!", color.THECOLORS['red'])
            print_text(font2, 170, 420, "Press Enter For Next Question", color.THECOLORS['red'])

        # display answers
        print_text(font1, 5, 170, "ANSWERS")
        print_text(font2, 20, 210, "1 - " + self.data[self.current + 1], self.colors[0])
        print_text(font2, 20, 240, "2 - " + self.data[self.current + 2], self.colors[1])
        print_text(font2, 20, 270, "3 - " + self.data[self.current + 3], self.colors[2])
        print_text(font2, 20, 300, "4 - " + self.data[self.current + 4], self.colors[3])

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wrong_answer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [color.THECOLORS['white'], color.THECOLORS['white'], color.THECOLORS['white'],
                           color.THECOLORS['white']]
            self.current += 6
            if self.current >= self.total:
                self.current = 0


def print_text(font, x, y, text, color=(255, 255, 255), shadow=True):
    if shadow:
        imgText = font.render(text, True, (0, 0, 0))

        screen.blit(imgText, (x - 2, y - 2))
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Trivia Game")
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)

trivia = Trivia('data.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()
    # clear the screen
    screen.fill((0, 0, 200))

    # display trivia data
    trivia.show_question()

    # update the display
    pygame.display.update()
