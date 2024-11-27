import pygame
import pymunk
import pymunk.pygame_util
from physics import *
from math import degrees
pygame.init()

class Goose:
    def __init__(self, x, y, vel, width = 40, height = 60):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.height = height
        self.goose_hitbox = create_rectangle(space, (40, 40), 40, 60)
        self.image = pygame.image.load("goose.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        pygame.transform.rotate(self.image, degrees(self.goose_hitbox.angle))
    
    def update(self, window):
        window.blit(self.image, (self.x, self.y))
        # pygame.Surface.blit(self.image, window)
        # pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))
        print("richard has big balls")
        self.x = self.goose_hitbox.position[0]
        self.y = self.goose_hitbox.position[1]
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and not keys[pygame.K_d]:  # Move Left
            self.goose_hitbox.velocity = (-500, self.goose_hitbox.velocity.y)  # Set x-velocity
        elif keys[pygame.K_d] and not keys[pygame.K_a]:  # Move Right
            self.goose_hitbox.velocity = (500, self.goose_hitbox.velocity.y)
        else:  # Stop Horizontal Movement if no key is pressed
            self.goose_hitbox.velocity = (0, self.goose_hitbox.velocity.y)
        if keys[pygame.K_w]:
            self.goose_hitbox.velocity = (self.goose_hitbox.velocity.x, -500)