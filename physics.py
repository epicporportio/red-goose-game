import pygame
import pymunk
import pymunk.pygame_util

space = pymunk.Space()
space.gravity = (0, 900)

def create_ground(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 450)
    shape = pymunk.Segment(body, (0, 150), (1250, 150), 10)  # Static line
    shape.friction = 0
    space.add(body, shape)
    
def create_rectangle(space, position, width, height):
    mass = 1
    moment = pymunk.moment_for_box(mass, (width, height))  # Calculate moment of inertia
    body = pymunk.Body(mass, moment)  # Dynamic body
    body.position = position
    shape = pymunk.Poly.create_box(body, (width, height))  # Create rectangle shape
    shape.elasticity = 0.5  # Bounciness
    shape.friction = 0    # Friction
    space.add(body, shape)
    return body