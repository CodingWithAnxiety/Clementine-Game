import pygame
import sprite
import environment

# Init the actual PYGAME lib
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic cube game test I")

# Basic colors
primary = '#2d1e22'
secondary = '#8f7085'
tertiary = '#f2eeed'

# We don't have player cube. Make it here.
player = sprite.Player(primary, 50, 50, 50, 0) 

#frame rate
clock = pygame.time.Clock()
FPS = 60

# Let's handle the grouping here. TODO

# We should group the eviroment here. Since we're not doing any complex enviroments yet
# We'll make this just a floor group.
enviroment_group = pygame.sprite.Group()

# Create the floor (enviroment.py TODO - REMOVED - TOP DOWN RPG INSTEAD!)
# floor = environment.Floor(secondary, screen_width, 50, screen_height - 50)
# enviroment_group.add(floor)

# Group for the player (we already have this)
player_group = pygame.sprite.Group() 
player_group.add(player)

# Create a sprite group to manage the player (and anything drawn on it?)
player_group = pygame.sprite.Group()
player_group.add(player)

# A main group to hold everything
all_sprites = pygame.sprite.Group()
all_sprites.add(enviroment_group)  # Add the floor group
all_sprites.add(player_group) # Add the player group

print(player_group)

# Game loop here.
running = True
while running:
    # Event handle
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
    # Print player position when P
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            print("Player position:", player.rect.x, player.rect.y)

    # Draw screen
    clock.tick(FPS)
    screen.fill(tertiary)

    # Rendering
    # Update (handles movement, etc.)
    all_sprites.update() 

    # REMOVED - TOP DOWN RPG INSTEAD!
    # if player.rect.bottom >= floor.rect.top:
    #     player.rect.bottom = floor.rect.top
    #     player.y_velocity = 0

    # Draw everything
    all_sprites.draw(screen) 



    # Floor with collision (TODO)
    pygame.display.update()

# Quit Python Application
pygame.quit()
