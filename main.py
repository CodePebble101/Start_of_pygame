import time

import pygame
from pygame.locals import *
import random
import sys

width, height = 600, 600
fraps = 30

pygame.init()
pygame.display.set_caption("Game for Cadaver")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Bahnschrift Light Condensed', 25)
wasted = pygame.font.SysFont('Bahnschrift Light Condensed', 100)


def DrawSpace():
    for i in range(100):
        screen.fill(pygame.Color('white'), (random.random() * width, random.random() * height, 1, 1))


un_width = 20

pos_x1 = 100
pos_y1 = 20

pos_x2 = width - pos_x1
pos_y2 = 20

pos_x3 = width // 2
pos_y3 = 20

pos_x4 = 20
pos_y4 = 20


def Rocket(x):
    pygame.draw.rect(screen, 'yellow', (x, 560, un_width, 10))
    DrawSpace()


def Barr(x_b, y_b):
    pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_b, y_b), 10)


act_x = 10
move = 15
i = 0
start_y = 0
speedup = 0


def Finish():
    screen.fill('black')
    textsurface2 = wasted.render('W A S T E D', False, (255, 0, 0))
    textsurface3 = myfont.render(f'Your score: {i}', False, (255, 0, 0))
    screen.blit(textsurface2, (width / 5, height / 2))
    screen.blit(textsurface3, (width / 5 + 130, height / 2 + 100))
    pygame.display.flip()
    time.sleep(3)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    screen.fill('black')
    textsurface = myfont.render(f'Score: {i}', False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))

    if keys[pygame.K_LEFT]:
        if act_x < 15:
            act_x = act_x
        else:
            act_x -= move

    if keys[pygame.K_RIGHT]:
        if act_x > width - (un_width + move + 5):
            act_x = act_x
        else:
            act_x += move

    if pos_y1 < height:
        pos_y1 += 5
    else:
        pos_x1 = random.randint(5, width - 5)
        pos_y1 = start_y
        i += 1

    if pos_y2 < height:
        pos_y2 += 10
    else:
        pos_x2 = random.randint(5, width - 5)
        pos_y2 = start_y
        i += 1

    if pos_y3 < height:
        pos_y3 += 7
    else:
        pos_x3 = random.randint(5, width - 5)
        pos_y3 = start_y
        i += 1

    if pos_y4 < height:
        pos_y4 += 8
    else:
        pos_x4 = random.randint(5, width - 5)
        pos_y4 = start_y
        i += 1

    Barr(pos_x1, pos_y1)
    Barr(pos_x2, pos_y2)
    Barr(pos_x3, pos_y3)
    Barr(pos_x4, pos_y4)
    if ((act_x - 5 <= pos_x3 <= act_x + un_width + 5) and (pos_y3 == 560)) or (
            (act_x - 5 <= pos_x2 <= act_x + un_width + 5) and (pos_y2 == 560)) or (
            (act_x - 5 <= pos_x1 <= act_x + un_width + 5) and (pos_y1 == 560)):
        Finish()
        break

    Rocket(act_x)
    clock.tick(fraps)
    if fraps <= 150:
        fraps += 0.1

    pygame.display.flip()
