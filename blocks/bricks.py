

import pygame, sys
import ball
from pygame.locals import *

BOARD_ROW = 12
BOARD_COL = 12

class BrickImage:

    def __init__(self, window, name):

        self.x = 0
        self.y = 0
        self.window = window
        self.name = name
        self.image = pygame.image.load(self.name)
        print("name: ", self.name)

    def Draw(self, x, y):

        #self.x = x
        #self.y = y
        self.window.blit(self.image, (x, y))
        #print("BrickImage.Draw: ", x, y)

class Brick:

    def __init__(self, window, image, minx, miny, maxx, maxy, name, ball):

        self.window = window
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.x = minx
        self.y = miny
        self.name = name
        self.brickImage = image
        self.disabled = False
        self.w = self.brickImage.image.get_width()
        self.h = self.brickImage.image.get_height()
        self.ball = ball

    def SetPosition(self, x, y):

        self.x = x
        self.y = y

    def Draw(self):

        if self.disabled is False:
            self.brickImage.Draw(self.x, self.y)

    def Collision(self, x, y, w, h):

        bxc = x + w/2
        byc = y + h/2

        if (byc > self.y) and (byc < (self.y +self.h)):
            if (bxc > self.x) and (bxc < (self.x + self.w)):
                if self.disabled == False:
                    self.ball.diry = -1 * self.ball.diry
                    self.ball.x = self.ball.x + 10
                self.disabled = True
                return True

        return False

    def Disable(self):

        self.disabled = True

class Bricks:

    def __init__(self, window, minx, miny, maxx, maxy, ball):

        self.window = window
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.bricks = []
        self.brickImages = []
        self.name = ""
        self.ball = ball

        for i in range(1, BOARD_ROW):
            self.name = "b" + str(i) + ".bmp"
            self.brickImages.append(BrickImage(window, self.name))

        index = 0
        for i in range(1, BOARD_ROW):
            #self.brickImages[i].x = i * 100
            x = (i-1) * 100
            for j in range(1, BOARD_COL):
                #self.brickImages[i].y = j * 25
                y = (j-1) * 50
                self.bricks.append(Brick(window, self.brickImages[i-1], minx, miny, maxx, maxy, self.name, self.ball))
                print("(i:j:index)", i, j, index)
                self.bricks[index].SetPosition(x, y)
                index = index + 1

    def Draw(self):

        for brick in self.bricks:
            brick.Draw()

    def Collision(self, x, y, w, h):

        for brick in self.bricks:
            if brick.Collision(x, y, w, h) == True:
                return True

        return False
    def AllBricksDisabled(self):

        state = False
        count = 0;

        for brick in self.bricks:
            if brick.disabled is False:
                count = count + 1

        if count == 0:
            self.Reset()
            state = True

        return state

    def Reset(self):

        index = 0
        state = True

        for brick in self.bricks:
            state = brick.disabled
            print("(state:index)", state, index)
            brick.disabled = False
