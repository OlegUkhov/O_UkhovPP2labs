import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
watch = pygame.image.load('mickeyclock.png')
wsize = (600, 800)
watch = pygame.transform.scale(watch, wsize)
rwatch = watch.get_rect(center=(300, 300))
hand1 = pygame.image.load('hand.png')
h1size = (220, 220)
hand1 = pygame.transform.scale(hand1, h1size)
hand2 = pygame.image.load('hand.png')
h2size = (240, 240)
hand2 = pygame.transform.scale(hand2, h2size)
clock = pygame.time.Clock()

import datetime as dt

def hands():
    n = dt.datetime.now()
    s = 6 * n.second
    m = 6 * n.minute
    return s, m

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

    seconds, minutes = hands()
    rhand1 = pygame.transform.rotate(hand1, -minutes)
    rhand2 = pygame.transform.rotate(hand2, -seconds)

    recthand1 = rhand1.get_rect(center=(300, 300))
    recthand2 = rhand2.get_rect(center=(300, 300))

    screen.fill((255, 255, 255))
    screen.blit(watch, rwatch)
    screen.blit(rhand2, recthand2)
    screen.blit(rhand1, recthand1)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()