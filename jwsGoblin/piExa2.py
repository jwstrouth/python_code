
import pygame

# initialize pygame
pygame.init()

# the main window caption
pygame.display.set_caption("PiGameExa")

screenWidth = 500
screenHeight = 480

# the main window
win = pygame.display.set_mode((screenWidth,screenHeight))

# the main window caption
pygame.display.set_caption("PiGameExa")

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
class player(object):
    walkRight = [
        pygame.image.load('R1.png'),
        pygame.image.load('R2.png'),
        pygame.image.load('R3.png'),
        pygame.image.load('R4.png'),
        pygame.image.load('R5.png'),
        pygame.image.load('R6.png'),
        pygame.image.load('R7.png'),
        pygame.image.load('R8.png'),
        pygame.image.load('R9.png')
    ]
    walkLeft = [
        pygame.image.load('L1.png'),
        pygame.image.load('L2.png'),
        pygame.image.load('L3.png'),
        pygame.image.load('L4.png'),
        pygame.image.load('L5.png'),
        pygame.image.load('L6.png'),
        pygame.image.load('L7.png'),
        pygame.image.load('L8.png'),
        pygame.image.load('L9.png')
    ]
    bulletSound = pygame.mixer.Sound("bullet.wav")
    hitSound = pygame.mixer.Sound("hit.wav")

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = True
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.x + 18, self.y + 10, 30, 56)
        self.shootloop = 0
        self.score = 0

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))

        for bullet in self.bullets:
            bullet.draw(win)

        self.hitbox = (self.x + 18, self.y + 10, 30, 56)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        text = font.render('Score: ' + str(self.score), 1, (0, 0, 0))
        win.blit(text, (350, 10))

    def update(self, enemy):

        if self.shootloop > 0:
            self.shootloop += 1
        if self.shootloop > 3:
            self.shootloop = 0

        if enemy.visible:
            if self.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.hitbox[1] + self.hitbox[3] > enemy.hitbox[1]:
                if self.hitbox[0] + self.hitbox[2] > enemy.hitbox[0] and self.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    self.hit()
                    self.score -= 5

        for bullet in self.bullets:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    self.hitSound.play()
                    enemy.hit()
                    self.score += 1
                    self.bullets.pop(self.bullets.index(bullet))

            if bullet.x < screenWidth and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                self.bullets.pop(self.bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.shootloop == 0:
            self.bulletSound.play()
            if self.left:
                facing = -1
            else:
                facing = 1
            if len(self.bullets) < 5:
                self.bullets.append(projectile(round(self.x + self.width //2), round(self.y + self.height //2), 6, (255,0,0), facing))
            self.shootloop = 1

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
        elif keys[pygame.K_RIGHT] and self.x < screenWidth - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0

        if not self.isJump:
            if keys[pygame.K_UP]:
                self.isJump = True
                #self.right = False
                #self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (screenWidth/2 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 10:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 11
                    pygame.quit()


class projectile(object):

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * self.facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    walkRightE = [
        pygame.image.load('R1E.png'),
        pygame.image.load('R2E.png'),
        pygame.image.load('R3E.png'),
        pygame.image.load('R4E.png'),
        pygame.image.load('R5E.png'),
        pygame.image.load('R6E.png'),
        pygame.image.load('R7E.png'),
        pygame.image.load('R8E.png'),
        pygame.image.load('R9E.png'),
        pygame.image.load('R10E.png'),
        pygame.image.load('R11E.png')
    ]
    walkLeftE = [
        pygame.image.load('L1E.png'),
        pygame.image.load('L2E.png'),
        pygame.image.load('L3E.png'),
        pygame.image.load('L4E.png'),
        pygame.image.load('L5E.png'),
        pygame.image.load('L6E.png'),
        pygame.image.load('L7E.png'),
        pygame.image.load('L8E.png'),
        pygame.image.load('L9E.png'),
        pygame.image.load('L10E.png'),
        pygame.image.load('L11E.png')
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 5
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 10, self.y + 4, 40, 56)
        self.health = 9
        self.visible = True

    def draw(self, win):
        self.move()

        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRightE[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeftE[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 9))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0],self.hitbox[1] - 20, 50 - (5* (9 - self.health)), 9))
            self.hitbox = (self.x + 10, self.y + 4, 40, 56)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("HIT")


def redrawGameWindow():

    global walkCount
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    #man2.draw(win)

    pygame.display.update()

def updateGameWindow():

    man.update(goblin)

# game loop
man = player(300, 410, 64, 64)
#man2 = player(0, 410, 64, 64, walkLeftE, walkRightE)
goblin = enemy(0, 415, 64, 64, 450)
font = pygame.font.SysFont('comicsans', 30, True)
run = True
while run:

    # delay loop
    clock.tick(27)

    # get input from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    updateGameWindow()

    redrawGameWindow()