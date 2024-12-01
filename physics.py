import pygame
import pymunk
import pymunk.pygame_util

space = pymunk.Space()
space.gravity = (0, 900)

# creation of the ground
def create_ground(space, width, height, position):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    shape = pymunk.Poly.create_box(body, (width, height))  # Static line
    shape.friction = 0.5
    space.add(body, shape)
    
# creation of a rectangle
def create_rectangle(space, position, width, height):
    mass = 1
    moment = pymunk.moment_for_box(mass, (width, height))  # Calculate moment of inertia
    body = pymunk.Body(mass, moment)  # Dynamic body
    body.position = position
    shape = pymunk.Poly.create_box(body, (width, height))  # Create rectangle shape
    shape.elasticity = 0.5  # Bounciness
    shape.friction = 0.5    # Friction
    space.add(body, shape)
    return body