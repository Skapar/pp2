import pygame

pygame.mixer.init()

pygame.mixer.music.load("song.mp3")

pygame.mixer.music.set_volume(0.7)

pygame.mixer.music.play()

while True:
    q = input()
    if q == 'p' :
        pygame.mixer.pause()
    elif q == 'r':
        pygame.mixer.unpause()
    elif q == 's':
        pygame.mixer.stop()
        break
clock = pygame.time.clock()

