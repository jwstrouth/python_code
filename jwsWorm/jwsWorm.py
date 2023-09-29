
import random, pygame, sys
from pygame.locals import *

winW = 1000
winH = 800
cellSize = 30
darkGray = (40, 40, 40)
darkGreen = (0, 155, 0)
green = (0, 255, 0)
red = (255, 0, 0)
bgColor = (0,0,0)
white = (255, 255, 255)
fps = 10
cellW = int(winW / cellSize)
cellH = int(winH / cellSize)
up = 'up'
down = 'down'
left = 'left'
right = 'right'
head = 0

class Game():

    def __init__(self, win):
        self.win = win
        self.clock = pygame.time.Clock()
        startx = random.randint(5, cellW - 6)
        starty = random.randint(5, cellH - 6)
        self.wormCoords = [{'x': startx, 'y': starty},
                      {'x': startx - 1, 'y': starty},
                      {'x': startx - 2, 'y': starty}]
        self.apple = self.getRandomLocation()
        print('Worm: '+str(self.wormCoords))
        print('Apple:'+str(self.apple))
        self.direction = right
        self.bFont = pygame.font.Font('freesansbold.ttf', 18)
        self.done = False
        self.score = len(self.wormCoords) - 3

    def run(self):

        while not self.done:
            self.getEvent()
            self.moveWorm()
            self.draw()
            self.wait()

    def reset(self):
        startx = random.randint(5, cellW - 6)
        starty = random.randint(5, cellH - 6)
        self.wormCoords = [{'x': startx, 'y': starty},
                           {'x': startx - 1, 'y': starty},
                           {'x': startx - 2, 'y': starty}]
        self.apple = self.getRandomLocation()
        self.direction = right
        self.done = False
        self.score = len(self.wormCoords) - 3

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and self.direction != right:
                    self.direction = left
                if (event.key == K_RIGHT or event.key == K_d) and self.direction != left:
                    self.direction = right
                if (event.key == K_UP or event.key == K_w) and self.direction != down:
                    self.direction = up
                if (event.key == K_DOWN or event.key == K_s) and self.direction != up:
                    self.direction = down
                else:
                    return event.key
        return None


    def draw(self):
        self.win.fill(bgColor)
        self.drawGrid()
        self.drawWorm()
        self.drawApple()
        self.drawScore()
        pygame.display.update()

    def wait(self):
        self.clock.tick(fps)

    def drawGrid(self):
        for x in range(0, winW, cellSize):  # draw vertical lines
            pygame.draw.line(self.win, darkGray, (x, 0), (x, winH))
        for y in range(0, winH, cellSize):  # draw horizontal lines
            pygame.draw.line(self.win, darkGray, (0, y), (winW, y))

    def drawWorm(self):
        for coord in self.wormCoords:
            x = coord['x'] * cellSize
            y = coord['y'] * cellSize
            wormSegmentRect = pygame.Rect(x, y, cellSize, cellSize)
            pygame.draw.rect(self.win, darkGreen, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cellSize - 8, cellSize - 8)
            pygame.draw.rect(self.win, green, wormInnerSegmentRect)

    def drawApple(self):
        x = self.apple['x'] * cellSize
        y = self.apple['y'] * cellSize
        appleRect = pygame.Rect(x, y, cellSize, cellSize)
        #print('Apple Rect: '+str(appleRect))
        pygame.draw.rect(self.win, red, appleRect)

    def moveWorm(self):

        # worm at edge of window
        if self.wormCoords[head]['x'] == -1 or self.wormCoords[head]['x'] == cellW \
                or self.wormCoords[head]['y'] == -1 or self.wormCoords[head]['y'] == cellH:
            self.done = True
            return

        # worm collided with itself
        for wormBody in self.wormCoords[1:]:
            if wormBody['x'] == self.wormCoords[head]['x'] and wormBody['y'] == self.wormCoords[head]['y']:
                self.done = True
                return

        if self.direction == up: newHead = {'x': self.wormCoords[head]['x'], 'y': self.wormCoords[head]['y'] - 1}
        if self.direction == down: newHead = {'x': self.wormCoords[head]['x'], 'y': self.wormCoords[head]['y'] + 1}
        if self.direction == left: newHead = {'x': self.wormCoords[head]['x'] - 1, 'y': self.wormCoords[head]['y']}
        if self.direction == right: newHead = {'x': self.wormCoords[head]['x'] + 1, 'y': self.wormCoords[head]['y']}

        # worm eaten apple
        if self.wormCoords[head]['x'] == self.apple['x'] and self.wormCoords[head]['y'] == self.apple['y']:
            # don't remove worm's tail segment
            self.apple = self.getRandomLocation()  # set a new apple somewhere
        else:
            del self.wormCoords[-1]

        self.wormCoords.insert(0, newHead)
        #print(self.wormCoords)

    def getRandomLocation(self):
        return {'x': random.randint(0, cellW - 1), 'y': random.randint(0, cellH - 1)}

    def showStart(self):
        titleFont = pygame.font.Font('freesansbold.ttf', 100)
        titleSurf1 = titleFont.render('JWS Wormy!', True, white, darkGreen)
        titleSurf2 = titleFont.render('JWS Wormy!', True, green)

        degrees1 = 0
        degrees2 = 0

        self.getEvent()

        while True:
            self.win.fill(bgColor)
            rotS1 = pygame.transform.rotate(titleSurf1, degrees1)
            rotR1 = rotS1.get_rect()
            rotR1.center = (winW / 2, winH / 2)
            self.win.blit(rotS1, rotR1)

            rotS2 = pygame.transform.rotate(titleSurf2, degrees1)
            rotR2 = rotS2.get_rect()
            rotR2.center = (winW / 2, winH / 2)
            self.win.blit(rotS2, rotR2)

            self.drawPressKeyMsg()

            if self.getEvent():
                return

            pygame.display.update()
            self.clock.tick(fps)

            degrees1 += 3
            degrees2 += 4

    def drawPressKeyMsg(self):
        pkSurf = self.bFont.render('Press a key to play.', True, darkGreen)
        pkRect = pkSurf.get_rect()
        pkRect.topleft = (winW - 200, winH - 30)
        self.win.blit(pkSurf, pkRect)

    def showGameOverScreen(self):
        gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
        gameSurf = gameOverFont.render('Game', True, white)
        overSurf = gameOverFont.render('Over', True, white)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (winW / 2, 10)
        overRect.midtop = (winH / 2, gameRect.height + 10 + 25)

        self.win.blit(gameSurf, gameRect)
        self.win.blit(overSurf, overRect)
        self.drawPressKeyMsg()
        pygame.display.update()
        pygame.time.wait(500)
        self.getEvent()
        while True:
            if self.getEvent():
                return
            pygame.time.wait(100)

    def drawScore(self):
        self.score = len(self.wormCoords) - 3
        scoreSurf = self.bFont.render('Score: %s' % (self.score), True, white)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (winW - 120, 10)
        self.win.blit(scoreSurf, scoreRect)

def main():

    pygame.init()
    fpsClock = pygame.time.Clock()
    win = pygame.display.set_mode((winW, winH))
    winFont = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('The Worm Game')

    g = Game(win)

    g.showStart()

    while True:
        g.run()
        g.showGameOverScreen()
        g.reset()


if __name__ == '__main__':
    main()
