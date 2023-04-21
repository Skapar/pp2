import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the player
player_size = (25, 25)
player_pos = [screen_width/2, screen_height/2]

# Set up the obstacles
obstacle_size = 50
obstacle_pos = [random.randint(0, screen_width-obstacle_size), random.randint(0, screen_height-obstacle_size)]

# Set up the collectibles
collectible_size = 25
collectible_pos = [random.randint(0, screen_width-collectible_size), random.randint(0, screen_height-collectible_size)]

# Set up the game loop
game_over = False
score = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size
            elif event.key == pygame.K_UP:
                player_pos[1] -= player_size
            elif event.key == pygame.K_DOWN:
                player_pos[1] += player_size
    
    # Move the obstacles
    obstacle_pos[1] += 5
    if obstacle_pos[1] > screen_height:
        obstacle_pos[0] = random.randint(0, screen_width-obstacle_size)
        obstacle_pos[1] = 0
    
    # Check for collision with the obstacles
    if player_pos[1] < obstacle_pos[1] + obstacle_size and player_pos[1] + player_size > obstacle_pos[1]:
        if player_pos[0] < obstacle_pos[0] + obstacle_size and player_pos[0] + player_size > obstacle_pos[0]:
            game_over = True
    
    # Move the collectibles
    collectible_pos[1] += 5
    if collectible_pos[1] > screen_height:
        collectible_pos[0] = random.randint(0, screen_width-collectible_size)
        collectible_pos[1] = 0
        score += 10
    
    # Check for collision with the collectibles
    if player_pos[1] < collectible_pos[1] + collectible_size and player_pos[1] + player_size > collectible_pos[1]:
        if player_pos[0] < collectible_pos[0] + collectible_size and player_pos[0] + player_size > collectible_pos[0]:
            collectible_pos[0] = random.randint(0, screen_width-collectible_size)
            collectible_pos[1] = 0
            score += 10
    
    # Draw the background
    screen.fill((0, 0, 0))
    
    # Draw the player
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size))