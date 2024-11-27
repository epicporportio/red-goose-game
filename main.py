import pygame
import pymunk
import pymunk.pygame_util
import player
from physics import *

pygame.init()

window = pygame.display.set_mode((1250, 750))

pygame.display.set_caption("Red Goose Game")

clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(window)
goose = player.Goose(40, 40, 5)
running = True

create_ground(space)

while running:
    clock.tick(300)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))
    goose.update(window)
    space.step(1 / 300.0)
    space.debug_draw(draw_options)
    pygame.display.flip()        