import pygame
from pygame.locals import *
import random

pygame.init()

FPS = 60
fps = pygame.time.Clock()

blue = pygame.Color(0, 0, 255)  #colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)

scrHeight = 600     #screen reso;ution
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

    def move(self):
        self.rect.move_ip(0, 10)
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
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, scrWidth - 60), 0) #coin spawn

    def move(self):
        self.rect.move_ip(0, 5)  #coins movement
        if self.rect.top > scrHeight:
            self.rect.top = random.randint(-600, -50)
            self.rect.centerx = random.randint(50, scrWidth - 50)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


p1 = Player()
e1 = enemy()      #creating objects
coin = Coin()

# Счетчик монет
coin_count = 0
font = pygame.font.SysFont('Impact', 36)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    p1.update()
    e1.move()     #checking for moving
    coin.move()

    if p1.rect.colliderect(coin.rect): #is coin sollected?
        coin_count += 1

        coin_sound = pygame.mixer.Sound('coinplus.mp3')
        coin_sound.play()

        coin.rect.top = random.randint(-600, -50)
        coin.rect.centerx = random.randint(50, scrWidth - 50)   #coin respawn

    if p1.rect.colliderect(e1.rect):    #cars collided?
        crash_sound = pygame.mixer.Sound('crash.mp3')
        crash_sound.play()

        scr.fill(red)
        game_over_font = pygame.font.SysFont('Impact', 50)
        game_over_text = game_over_font.render("GAME OVER", True, white) #game over screen
        score_text = font.render(f"COINS: {coin_count}", True, white)

        scr.blit(game_over_text, (scrWidth // 2 - 120, scrHeight // 2 - 50))
        scr.blit(score_text, (scrWidth // 2 - 100, scrHeight // 2 + 10))
        pygame.display.update()

        pygame.time.delay(2000)
        pygame.quit()
        exit()

    scr.fill(gray)

    grass_color = pygame.Color(0, 200, 0)
    grass_width = 40  
    pygame.draw.rect(scr, grass_color, (0, 0, grass_width, scrHeight))  #grass
    pygame.draw.rect(scr, grass_color, (scrWidth - grass_width, 0, grass_width, scrHeight)) 

    # Рисуем игрока, врага и монету
    p1.draw(scr)
    coin.draw(scr)
    e1.draw(scr)

    # Отображаем счетчик монет
    score_text = font.render(f"COINS: {coin_count}", True, white)
    scr.blit(score_text, (scrWidth - 140, -5)) # Верхний правый угол

    pygame.display.update()
    fps.tick(FPS)

