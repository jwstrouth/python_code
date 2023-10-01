
import pygame
#from pygame.locals import *

class Ball:

    def __init__(self, window, minx, miny, maxx, maxy):

        self.window = window
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.x = maxx / 2
        self.y = maxy - 10
        self.ball = pygame.image.load('blocksBall.bmp')
        self.color = (255, 255, 255)
        self.ball.set_colorkey(self.color)
        self.dirx = 1
        self.diry = 1
        self.w = self.ball.get_width()
        self.h = self.ball.get_height()

    def Update(self):

        if self.x >= (self.maxx - self.ball.get_width()):
            self.dirx = -1
        if self.x <= self.minx:
            self.dirx = 1
        self.x = self.x + 1 * self.dirx

        if self.y >= (self.maxy - self.ball.get_height()):
            self.diry = -1
        if self.y <= self.miny:
            self.diry = 1;
        self.y = self.y + 1 * self.diry

    def Draw(self):

       self.window.blit(self.ball, (self.x, self.y))

    def Reset(self):

        self.x = self.maxx / 2
        self.y = self.maxy - 10
        self.dirx = 1
        self.diry = 1
