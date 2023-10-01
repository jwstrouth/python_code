#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY1 = 100, 100, 100
GREY2 = 200, 200, 200
SPOSX = 500
SPOSY = 600


class Sprite(pygame.sprite.Sprite):

    def loadimage(self, name, colorkey=None):
        try:
            image = pygame.image.load(name)
        except pygame.error:
            print('Cannot load image: ', name)

        image = image.convert()

        return image, image.get_rect()

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.loadimage(name)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self, x, y):
        self.rect.move(x, y)


class Ball:

    def __init__(self, screen, width, height):

        self.w = 10
        self.h = 10
        self.x = SPOSX + 40
        self.y = SPOSY - 10
        self.s = screen
        self.c = RED
        self.width = width
        self.height = height
        self.dx = 3
        self.dy = -3
        self.ballS = pygame.image.load('ball1.png')
        self.ballS = pygame.transform.scale(self.ballS, (20, 20))
        # self.ball = Sprite('ball1.png')
        # self.ballsprite = pygame.sprite.RenderPlain(self.ball)


    def draw(self):

        x = self.x
        y = self.y
        # s = self.s
        # c = self.c
        # w = self.w
        # h = self.h
        # pygame.draw.circle(s, c, (x, y), w, h)
        self.s.blit(self.ballS, (x, y))
        # pygame.display.flip()

        # self.ballsprite.update(x, y)
        # self.ballsprite.draw(self.s)

    def move(self):

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        if self.x < self.w or self.x > (self.width - self.w):
            self.dx = -self.dx
        if self.y < self.h or self.y > (self.height - self.h):
            self.dy = -self.dy

    def direction(self, d):

        if d:
            self.dy *= -1

    def update(self):

        self.move()

    def collide(self, x, w, y, h):

        if x < self.x < x + w:
            if y < self.y < y + h:
                return True
        else:
            return False


class Paddle:

    def __init__(self, screen):

        self.w = 80
        self.h = 20
        self.x = SPOSX
        self.y = SPOSY
        self.s = screen
        self.c = GREY1
        self.dx = 5
        self.mouseD = False
        self.mouseU = False
        self.mouseM = False
        self.lock = False
        self.paddleS = pygame.image.load('paddle.png')
        self.paddleS = pygame.transform.scale(self.paddleS, (80, 20))

    def draw(self):

        # pygame.draw.rect(self.s, self.c, (self.x, self.y, self.w, self.h))
        self.s.blit(self.paddleS, (self.x, self.y))
        # pygame.display.flip()

    def move(self, d):

        if d == 1:
            self.x += self.dx
        if d == 0:
            self.x -= self.dx

    def mousemove(self):

        mouse = pygame.mouse.get_pos()
        x = self.x
        y = self.y
        w = self.w
        h = self.h

        if not self.lock:
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                self.c = GREY2
                if self.mouseD:
                    self.lock = True
            else:
                self.c = GREY1
        else:
            self.x = mouse[0] - w / 2


class Brick:
    COLORS = {1: GREEN, 2: BLUE, 3: RED}

    def __init__(self, screen, x, y, hits, index):
        width = 75
        height = 20
        self.hit = hits
        self.s = screen
        self.c = Brick.COLORS[hits]
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.dirtyflag = 1
        self.brickSR = pygame.image.load('brickred.png')
        self.brickSR = pygame.transform.scale(self.brickSR, (width, height))
        self.brickSG = pygame.image.load('brickgreen.png')
        self.brickSG = pygame.transform.scale(self.brickSG, (width, height))
        self.brickSB = pygame.image.load('brickblue.png')
        self.brickSB = pygame.transform.scale(self.brickSB, (width, height))
        self.draw()
        self.state = True
        self.index = index

    def draw(self):

        x = self.x
        y = self.y
        w = self.w
        h = self.h
        s = self.s
        c = self.c

        if  self.c == GREEN:
                self.s.blit(self.brickSG, (x, y))
        if self.c == BLUE:
                self.s.blit(self.brickSB, (x, y))
        if self.c == RED:
                self.s.blit(self.brickSR, (x, y))

        # pygame.draw.rect(s, c, (x, y, w, h))
        # pygame.display.flip()

    def hitme(self):

        self.hit -= 1
        if self.hit <= 0:
            self.state = False
            print("Dead: " + str(self.index) + ":" + str(self.hit))
            return self.state
        else:
            self.c = Brick.COLORS[self.hit]
        # print((self.index, self.hit))
        return self.state

    def reset(self):
        self.hit = 3
        self.state = True
        self.c = Brick.COLORS[self.hit]


class Game:

    def __init__(self):

        pygame.init()
        self.width = 1000
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Breakout')
        self.clock = pygame.time.Clock()
        self.bricks = {}
        self.paddle = Paddle(self.screen)
        self.ball = Ball(self.screen, self.width, self.height)
        index = 0
        for x in range(5, (self.width - 5), 100):
            self.add_brick(x + 5, 50, 3, index)
            index += 1
            self.add_brick(x + 5, 80, 3, index)
            index += 1
            self.add_brick(x + 5, 110, 3, index)
            index += 1
            self.add_brick(x + 5, 140, 3, index)
            index += 1
            self.add_brick(x + 5, 170, 3, index)
            index += 1
        print(len(self.bricks))
        self.run()

    def add_brick(self, x, y, hits, index):

        brick = Brick(self.screen, x, y, hits, index)
        self.bricks[index] = brick
        # print((brick.x, brick.y, brick.w, brick.h))

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.paddle.mouseD = True
                    self.paddle.mouseU = False
                    self.paddle.mouseM = False
                    # print("Down")
                if event.type == pygame.MOUSEBUTTONUP:
                    self.paddle.mouseD = False
                    self.paddle.mouseU = True
                    self.paddle.mouseM = False
                    self.paddle.lock = False
                    # print("Up")
                if event.type == pygame.MOUSEMOTION:
                    self.paddle.mouseM = True

            self.update()
            self.screen.fill((0, 0, 0))
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

    def reset(self):
        for index in self.bricks:
            brick = self.bricks[index]
            brick.reset()

    def check(self):
        count = 0
        for index in self.bricks:
            brick = self.bricks[index]
            if brick.state:
                count += 1
        return count

    def update(self):

        self.ball.update()

        for index in self.bricks:
            brick = self.bricks[index]
            if brick.state:
                if self.ball.collide(brick.x, brick.w, brick.y, brick.h):
                    brick.hitme()
                    self.ball.direction(True)
            index += 1

        if self.check() == 0:
            print('*** All bricks destryed ***')
            self.reset()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.paddle.move(0)
        if keys[K_RIGHT]:
            self.paddle.move(1)

        if self.ball.collide(self.paddle.x, self.paddle.w, self.paddle.y, self.paddle.h):
            self.ball.direction(True)

        self.paddle.mousemove()

    def draw(self):

        for index in self.bricks:
            brick = self.bricks[index]
            if brick.state:
                brick.draw()
            index += 1
        self.paddle.draw()
        self.ball.draw()


if __name__ == "__main__":
    game = Game()
    # game.run()
