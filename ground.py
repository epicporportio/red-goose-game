from physics import *
import pygame
import pymunk

# ground class
class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height, position):
        super().__init__()
        self.width = width
        self.height = height
        self.position = position
        pymunk_is_gay_x = self.position[0]
        pymunk_is_gay_y = self.position[1]
        x = pymunk_is_gay_x + self.width/2
        y = pymunk_is_gay_y + self.height/2
        self.ground_physics_hitbox = create_ground(space, width, height, (x, y))
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.ground_hitbox = pygame.Rect(x-625, y-10, self.width, self.height)
    
    # updates the ground
    def update(self, window):
        window.blit(self.image, self.position)