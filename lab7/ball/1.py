import pygame
import sys
 
FPS = 60
W = 700 
H = 300 
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RED = (139, 0, 0)
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 

x = W // 2
y = H // 2
r = 25
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 5
            elif i.key == pygame.K_RIGHT:
                x += 5
            elif i.key == pygame.K_DOWN:
                y += 5
            elif i.key == pygame.K_UP:
                y -= 5 
            
 
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)
 