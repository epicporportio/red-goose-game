import pygame
import pymunk
import pymunk.pygame_util
import player
from player import Goose
from physics import *
from ground import Ground

# initialize pygame
pygame.init()

window = pygame.display.set_mode((1250, 750))

pygame.display.set_caption("Red Goose Game")

clock = pygame.time.Clock()
fps = 300
draw_options = pymunk.pygame_util.DrawOptions(window)
goose = player.Goose(40, 40)
ground = Ground(1250, 20, (0, 600))
sprites = pygame.sprite.Group()
sprites.add(goose)
running = True

# game loop
while running:
    
    # framerate
    clock.tick(fps)
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))
    goose.update(window, ground.ground_hitbox)
    ground.update(window)
    space.step(1 / 300.0)
    # space.debug_draw(draw_options)
    pygame.display.flip() 