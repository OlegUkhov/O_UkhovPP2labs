import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
speed = 20
radius = 25
x, y = 0, 0
clock = pygame.time.Clock()

working = True
while working:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed <= 500 - radius * 2:
        y += speed
    if keys[pygame.K_LEFT] and x - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed <= 500 - radius * 2:
        x += speed

    pygame.draw.circle(screen, (255, 0, 0), (x + radius, y + radius), radius)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()