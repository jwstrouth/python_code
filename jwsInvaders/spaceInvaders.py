#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

pygame.mouse.set_visible(0)

shipImage = pygame.image.load("player1.gif")
ship_top = screen.get_height() - shipImage.get_height()
ship_left = screen.get_width()/2 - shipImage.get_width()/2

invader = pygame.image.load("alien1.gif")
print(invader.get_rect())

shoot_y = 0
shoot_x = 0

invaderList = []

def setUpInvaders():
    y = 0
    num_row = 3
    num_invaders_per_row = 5
    w = 100

    while y <= w * num_row:
        x = w
        while x <= w * num_invaders_per_row:
            invaderList.append(Rect(x, y, 80, 71))
            x = x + w
        y = y + w

    return invaderList

def drawInvaders():
    for i in invaderList:
        screen.blit(invader, i)

bulletList = []

def drawBullets():
    global shoot_x, shoot_y

    for s in bulletList:
        if s.y > 0:
            s.update()
            s.draw()
        else:
            bulletList.pop(bulletList.index(s))
            print("Remove bullet: "+str(s))

class Ship():
    def __init__(self, screen, image):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image = image
        self.w = self.screen.get_height() - self.image.get_height()
        self.h = self.screen.get_width()/2 - self.image.get_width()/2
        self.top = self.screen.get_height() - self.image.get_height()

    def draw(self, x, y):
        self.x = x-self.image.get_width()/2
        self.y = y
        self.screen.blit(self.image, (self.x, self.top))

class Bullet():
    def __init__(self, x, y, screen, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.shot = pygame.image.load("shot.gif")
        self.screen = screen

    def draw(self):
        self.screen.blit(self.shot, (self.x, self.y))

    def update(self):
        #print("Bullet: "+str(self.y))
        if self.y > 0:
            self.y -= 5
            #print("Bullet true")
            return 1
        else:
            #print("Bullet false")
            return 0



setUpInvaders()

ship = Ship(screen, shipImage)
shootloop = 0

while True:
    clock.tick(60)
    screen.fill((0, 0, 0))
    drawInvaders()
    x,y = pygame.mouse.get_pos()
    ship.draw(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if shootloop > 0:
            shootloop += 1
        if shootloop > 5:
            shootloop = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shootloop == 0:
            shoot_y = 500
            shoot_x = x
            if len(bulletList) < 5:
                s = Bullet(shoot_x, shoot_y, screen, 800, 600)
                bulletList.append(s)
                print("Add bullete: "+str(s))
            shootloop = 1

    drawBullets()

    pygame.display.update()