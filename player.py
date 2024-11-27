import pygame
import pymunk
import pymunk.pygame_util
pygame.init()

class Goose:
    def __init__(self, x, y, vel, width = 40, height = 60):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.height = height
    
    def update(self, window):
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and self.x - self.vel >= 0:
            self.x -= self.vel
            
        if keys[pygame.K_d] and self.x + self.vel <= 1250 - self.width:
            self.x += self.vel
            
        if keys[pygame.K_w] and self.y - self.vel >= 0:
            self.y -= self.vel
            
        if keys[pygame.K_s] and self.y + self.vel <= 750 - self.height:
            self.y += self.vel