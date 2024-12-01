import pygame
import pymunk
import pymunk.pygame_util
from physics import *
from math import degrees
pygame.init()

# Goose class(player class)
class Goose(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 40, height = 40):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.goose_hitbox = create_rectangle(space, (40, 40), width, height)
        self.image = pygame.image.load("goose.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
    
    # updates the player
    def update(self, window):
        self.new_image = pygame.transform.rotate(self.image, round(degrees(self.goose_hitbox.angle)))
        print(round(degrees(self.goose_hitbox.angle)))
        window.blit(self.new_image, (self.x, self.y))
        # pygame.Surface.blit(self.image, window)
        # pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))
        pymunk_is_gay_x = self.goose_hitbox.position[0]
        pymunk_is_gay_y = self.goose_hitbox.position[1]
        self.x = pymunk_is_gay_x - self.image.get_width()/2
        self.y = pymunk_is_gay_y - self.image.get_height()/2
        keys = pygame.key.get_pressed()
        
        # movement of the player
        if keys[pygame.K_a] and not keys[pygame.K_d]:  # Move Left
            self.goose_hitbox.velocity = (-200, self.goose_hitbox.velocity.y)  # Set x-velocity
        elif keys[pygame.K_d] and not keys[pygame.K_a]:  # Move Right
            self.goose_hitbox.velocity = (200, self.goose_hitbox.velocity.y)
        else:  # Stop Horizontal Movement if no key is pressed
            self.goose_hitbox.velocity = (0, self.goose_hitbox.velocity.y)
        if keys[pygame.K_w]:
            self.goose_hitbox.velocity = (self.goose_hitbox.velocity.x, -300)