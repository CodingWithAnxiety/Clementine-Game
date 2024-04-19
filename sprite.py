import pygame
from itertools import cycle

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.load_sprites(width, height)

        self.direction = "down"  # Start our direction facing the camera
        self.frame = 0 # Set the default frame to idle.
        self.frame_index = 0 # I hate declaring this in the init, but... Whatever, it works. We're fine.

        self.image = self.sprites["down"][0]
        self.rect = self.image.get_rect()

        # Set our initial position
        self.rect.x = x
        self.rect.y = y

        # Definte the last animation change!
        self.last_animation_change = 0

        # Sets our speed.
        self.speed = 5

    def load_sprites(self, width, height):
            #TODO Update with new sprites (Let's do that *TODAY!*)
        self.sprites = {
            "down": [
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Down_Idle.png").convert_alpha(), (width, height)),
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Down_Walk1.png").convert_alpha(), (width, height)),
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Down_Walk2.png").convert_alpha(), (width, height))
            ],
            "up": [
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Up_Idle.png").convert_alpha(), (width, height)),
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Up_Walk1.png").convert_alpha(), (width, height)),
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Up_Walk2.png").convert_alpha(), (width, height))
            ], 
            # "side": [
            #     pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Idle.png").convert_alpha(), (width, height)),
            #     pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Walk1.png").convert_alpha(), (width, height)), 
            #     pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Walk2.png").convert_alpha(), (width, height))
            # ],        This adds unneeded complexity to the overall code. Will renove later.
            "left": [
                # We have no left sprites, so we'll just flip the right ones and use those!
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Idle.png").convert_alpha(), (width, height)), True, False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Walk1.png").convert_alpha(), (width, height)), True, False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Walk2.png").convert_alpha(), (width, height)), True, False)
            ],
            "right": [
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Idle.png").convert_alpha(), (width, height)),
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Walk1.png").convert_alpha(), (width, height)),
                pygame.transform.scale(pygame.image.load(f"./img/sprites/player/Side_Walk2.png").convert_alpha(), (width, height))
            ] 
        }

    def update(self):
        # Check the movement keys. If so, let's move that direction and set our self.direction to that direction.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "left"
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "right"
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = "up"
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = "down"
        if keys[pygame.K_p]:
            print("Player position:", self.rect.x, self.rect.y)
            print(self.direction)
        
        self.handle_animation()

    def movement_check(self):
        keys = pygame.key.get_pressed()
        moving = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]
        return moving

    def handle_animation(self):
        # The cooldown here ensures we're only changing frames every 6 frame
        animation_cooldown = 250
        now = pygame.time.get_ticks()
        # Import the movement check as moving.
        moving = self.movement_check()

        # We need to comare to the cooldown time set above.
        if now - self.last_animation_change > animation_cooldown:
            self.last_animation_change = now
            # If we pass the cooldown, check the return of moving. If moving = true.
            if moving:
                # We're moving, play the animation based on the frames in init.
                walking_frames = [2, 0, 1, 0]  # Walk 2 -> Idle -> Walk 1

                # I pray to god I never have to do this again. 
                self.frame = walking_frames[self.frame_index]
                self.frame_index = (self.frame_index + 1) % len(walking_frames) # This code is driving me absolutely mad. Thanks, Codecademy community for doing this for me.

                # Test print to ensure that the animation frames are playing correctly
                print("Walking frame:", self.frame)
            else:
                # We're not moving, set frame to 0 (Idle)
                self.frame = 0
                self.frame_index = 0 # . . . let's *not* forget this next time. Sets the frame_index to 0 when not moving.
        
        # We need to be sure we're walking the right direction AND updating our animation every frame! This handles that.
        self.image = self.sprites[self.direction][self.frame]
        print (self.frame)
