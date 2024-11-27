import pygame
import pymunk
import pymunk.pygame_util
import player
pygame.init()

window = pygame.display.set_mode((1250, 750))

pygame.display.set_caption("Red Goose Game")

clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 900)
draw_options = pymunk.pygame_util.DrawOptions(window)

def create_ground(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 450)
    shape = pymunk.Segment(body, (0, 150), (1250, 150), 10)  # Static line
    shape.friction = 0.9
    space.add(body, shape)
    
def create_rectangle(space, position, width, height):
    mass = 1
    moment = pymunk.moment_for_box(mass, (width, height))  # Calculate moment of inertia
    body = pymunk.Body(mass, moment)  # Dynamic body
    body.position = position
    shape = pymunk.Poly.create_box(body, (width, height))  # Create rectangle shape
    shape.elasticity = 0.5  # Bounciness
    shape.friction = 0.8    # Friction
    space.add(body, shape)
    return shape

running = True

create_ground(space)

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    window.fill((0, 0, 0))
    space.step(1 / 60.0)
    space.debug_draw(draw_options)
    pygame.display.flip()        