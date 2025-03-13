import pygame

pygame.init()

pygame.mixer.init()
screen = pygame.display.set_mode((650, 650))
screen.fill((0, 0, 0))

font = pygame.font.Font(None, 50)
pygame.draw.rect(screen, (255, 255, 255), (50, 50, 550, 100), border_radius=20)
pygame.draw.rect(screen, (255, 255, 255), (50, 200, 550, 100), border_radius=20)
pygame.draw.rect(screen, (255, 255, 255), (50, 350, 550, 100), border_radius=20)
pygame.draw.rect(screen, (255, 255, 255), (50, 500, 550, 100), border_radius=20)

t1 = font.render('Play - P', True, (0, 0, 0))
t2 = font.render('Stop - S', True, (0, 0, 0))
t3 = font.render('Next - N', True, (0, 0, 0))
t4 = font.render('Previous - Z', True, (0, 0, 0))

screen.blit(t1, (325 - t1.get_width() // 2, 100 - t1.get_height() // 2))
screen.blit(t2, (325 - t2.get_width() // 2, 250 - t2.get_height() // 2))
screen.blit(t3, (325 - t3.get_width() // 2, 400 - t3.get_height() // 2))
screen.blit(t4, (325 - t4.get_width() // 2, 550 - t4.get_height() // 2))

songs = ['Lab7PP2task2/Arctic Monkeys - Fluorescent Adolescent.mp3', 'Lab7PP2task2/Gorillaz - On Melancholy Hill.mp3', 'Lab7PP2task2/twenty one pilots - Paladin Strait.mp3']
song = 0

def player(whichsong):
    pygame.mixer.music.load(songs[whichsong])
    pygame.mixer.music.play() 

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player(song)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                song = (song + 1) % len(songs)
                player(song)
            elif event.key == pygame.K_z:
                song = (song - 1) % len(songs)
                player(song)

    pygame.display.flip()
pygame.quit()