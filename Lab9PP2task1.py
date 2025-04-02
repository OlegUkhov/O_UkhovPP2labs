import pygame
from pygame.locals import *
import random

pygame.init()

enemyspeed = 7
FPS = 60
fps = pygame.time.Clock()

blue = pygame.Color(0, 0, 255)  #colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)

scrHeight = 600     #screen resolution
scrWidth = 300 

scr = pygame.display.set_mode((scrWidth, scrHeight))
scr.fill(white)
pygame.display.set_caption('Racer')

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, scrWidth - 60), random.randint(-600, -50))  # enemy spawn
        self.enemyspeed = enemyspeed

    def move(self, enemyspeed):    
        self.rect.move_ip(0, enemyspeed)
        if self.rect.top > scrHeight:
            self.rect.top = random.randint(-600, -50)
            self.rect.centerx = random.randint(60, scrWidth - 60) #enemy spawn

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (scrWidth // 2, scrHeight - 80) #initial position of player

    def update(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 40:
            if pressed[K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.image = pygame.transform.rotate(pygame.image.load('Player.png'), 10) #left rotation 

        if self.rect.right < scrWidth - 40:
            if pressed[K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.image = pygame.transform.rotate(pygame.image.load('Player.png'), -10)  #right rotation

        if not (pressed[K_LEFT] or pressed[K_RIGHT]):
            self.image = pygame.image.load('Player.png') #normal angle

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.baseCoin = pygame.image.load('coin.png')
        self.bigCoin = pygame.transform.scale(self.baseCoin, (int(self.baseCoin.get_width() * 1.5), int(self.baseCoin.get_height() * 1.5)))
        self.big = False                                                                                    #big coin spawn
        self.bigSize()
        self.rect.center = (random.randint(60, scrWidth - 60), 0) #coin spawn

    def bigSize(self):
        if random.randint(0, 4) == 0:  #20% chance 
            self.big = True
            self.image = self.bigCoin
        else:
            self.big = False
            self.image = self.baseCoin
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.move_ip(0, 5)  #coins movement
        if self.rect.top > scrHeight:
            self.bigSize()
            self.rect.top = random.randint(-600, -50)
            self.rect.centerx = random.randint(50, scrWidth - 50)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


p1 = Player()
e1 = enemy()      #creating objects
coin = Coin()

coins = 0
lastLevelUp = 0
font = pygame.font.SysFont('Impact', 36) #coin counter

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    p1.update()
    coin.move()

    if p1.rect.colliderect(coin.rect): #is coin sollected?
        if coin.big:
            coins += 2
        else:
            coins += 1

        coinSound = pygame.mixer.Sound('coinplus.mp3') #sound of the coins picking
        coinSound.play()

        coin.bigSize()
        coin.rect.top = random.randint(-600, -50)
        coin.rect.centerx = random.randint(50, scrWidth - 50)
        
        if coins > 0 and coins % 5 == 0 and coins > lastLevelUp:    #level up for each 5 coins
            enemyspeed += 3
            lastLevelUp = coins

    if p1.rect.colliderect(e1.rect):    #cars collided?
        crashSound = pygame.mixer.Sound('crash.mp3')
        crashSound.play()

        scr.fill(red)
        font = pygame.font.SysFont('Impact', 50)
        goText = font.render("GAME OVER", True, white)    #game over screen
        scoreText = font.render(f"COINS: {coins}", True, white)

        scr.blit(goText, (scrWidth // 2 - 120, scrHeight // 2 - 50))
        scr.blit(scoreText, (scrWidth // 2 - 100, scrHeight // 2 + 10))
        pygame.display.update()

        pygame.time.delay(2000) #waiting before windows closing
        pygame.quit()
        exit()

    scr.fill(gray)

    grass = pygame.Color(0, 200, 0)
    grassWidth = 40  
    pygame.draw.rect(scr, grass, (0, 0, grassWidth, scrHeight))  #grass
    pygame.draw.rect(scr, grass, (scrWidth - grassWidth, 0, grassWidth, scrHeight)) 

    p1.draw(scr)
    coin.draw(scr)
    e1.draw(scr)

    scoreText = font.render(f"COINS: {coins}", True, white)   #coins counter
    scr.blit(scoreText, (scrWidth - 140, -5)) 

    e1.move(enemyspeed)
    pygame.display.update()
    fps.tick(FPS)