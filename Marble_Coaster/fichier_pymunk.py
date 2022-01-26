import sys
import pygame
from pygame.locals import *
import pymunk
from numpy import *

def add_ball(space):
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    x = random.randint(15, 585)
    body.position = x, 550
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9
    space.add(body, shape)
    return shape

def draw_ball(screen, ball):
    p = int(ball.body.position.x), 600 - int(ball.body.position.y)
    pygame.draw.circle(screen, (0, 0, 255), p, int(ball.radius), 2)

def add_static_L(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255, 0), 5)
    l2 = pymunk.Segment(body, (-150, 0), (-150, 50), 5)
    space.add(l1, l2)
    return l1, l2

def to_pygame(p):
    return int(p.x), int(- p.y + 600)

def draw_lines(screen, lines):
    for line in lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(screen, (250, 2, 50), False, [p1, p2])

def add_L(space):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_limit_body.position = (200,300)

    body = pymunk.Body(10, 10000)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)
    l1.elasticity = 0.9
    l2.elasticity = 0.9

    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100, 0), (0, 0), 0, joint_limit)

    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1, l2


def affichage_départ():
    pygame.init()
    screen = pygame.display.set_mode((1200, 1200))
    pygame.display.set_caption(" Affichage jeu de la bille ")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, - 981)

    lines = add_L(space)
    ball = add_ball(space)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        screen.fill((255, 255, 255))

        draw_ball(screen, ball)
        draw_lines(screen, lines)

        space.step(1/50)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    sys.exit(affichage_départ())



