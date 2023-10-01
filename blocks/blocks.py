
import pygame, sys, random
from pygame.locals import *
import ball
import bricks
pygame.init()

# color
BACKGROUND = (0, 0, 255)

# game setup
FPS = 200*5
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 800

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('BLOCKS')
area1 = pygame.image.load("blocksArea1.bmp")
area1 = pygame.transform.scale(area1, (1100, 800))

ball = ball.Ball(window, 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
bricks = bricks.Bricks(window, 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, ball)

collision = False

def drawBall() :
    global ball

    ball.Draw()

def drawBrick():
    global bricks

    bricks.Draw()

def upDate():
    global ball
    global collision

    ball.Update()

    if bricks.Collision(ball.x, ball.y, ball.w, ball.h) == True:
        collision = True
    else:
        collision = False

    if bricks.AllBricksDisabled() is True:
        bricks.Reset()
        print("Reset")
        ball.Reset()

def main() :
    looping = True

    while looping :

        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        window.fill(BACKGROUND)
        window.blit(area1, (0, 0))
        upDate()
        drawBall()
        drawBrick()
        pygame.display.update()
        fpsClock.tick(FPS)

main()