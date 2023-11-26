import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective
import numpy as np
import math

angle_x = 0
angle_y = 0
mouse_dragging = False
prev_mouse_pos = None

# the parameters of the legs
vertices = (
    (0, 0, 0),
    (0, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 4, 7, 3),
    (1, 5, 6, 2)
)

theta_x = 0
theta_y = 0
theta_z = 0

translate_x_rotating = 0
translate_y_rotating = 0
translate_z_rotating = 0

translate_x = 0
translate_y = 0
translate_z = 0

rotation_center = np.array([0.3, 0.0, 0.0])
rotation_center2 = np.array([1.9, 0.0, 0.0])



def draw_box(x, y, z, width, height, depth):
    vertices = [
        [x, y, z],
        [x + width, y, z],
        [x + width, y + height, z],
        [x, y + height, z],
        [x, y, z + depth],
        [x + width, y, z + depth],
        [x + width, y + height, z + depth],
        [x, y + height, z + depth]
    ]

    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_boxy_animal():
    glPushMatrix()

    # Body
    glColor3f(0.5, 0.5, 0.5)
    draw_box(0, 0, 0, 2, 1, 1)

    # neck
    draw_box(0,1,0.25,0.5,1,0.5)

    # head
    draw_box(-0.5,1.5,0.25,0.5,0.3,0.5)
    glPopMatrix()

def draw_leg_1():
    global theta_z
    glPushMatrix()
    glTranslatef(rotation_center[0], rotation_center[1], rotation_center[2])
    glColor3f(0.3, 0.3, 0.3)
    glRotatef(theta_z, 0, 0, 1)
    glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])
    # Translate to the current position
    glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)

    draw_box(*(0.2,-0.5,0.0), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_1_2(x,y,z):
    global theta_z, translate_x, translate_z
    glPushMatrix()
    # glTranslatef(rotation_center[0], rotation_center[1], rotation_center[2])

    glTranslatef(x,y,z)
    glColor3f(0.3, 0.3, 0.3)
    # glRotatef(theta_z, 0, 0, 1)
    # glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])
    # glTranslatef(-x, -y, -z)
    # Translate to the current position
    glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)
    draw_box(*(0.2,-1,0.0), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_2():
    global theta_z
    glPushMatrix()
    glTranslatef(rotation_center2[0], rotation_center2[1], rotation_center2[2])
    glColor3f(0.3, 0.3, 0.3)
    glRotatef(-theta_z, 0, 0, 1)
    glTranslatef(-rotation_center2[0], -rotation_center2[1], -rotation_center2[2])

    # Translate to the current position
    glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)

    draw_box(*(1.8, -0.5, 0.0), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_2_2(x,y,z):
    global theta_z, translate_x, translate_z
    glPushMatrix()
    glTranslatef(x,y,z)
    # glTranslatef(rotation_center2[0], rotation_center2[1], rotation_center2[2])
    glColor3f(0.3, 0.3, 0.3)
    # glRotatef(-theta_z, 0, 0, 1)
    # glTranslatef(-rotation_center2[0], -rotation_center2[1], -rotation_center2[2])

    # Translate to the current position
    # glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)
    # glTranslatef(translate_x, translate_y, translate_z)
    draw_box(*(1.8, -1, 0.0), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_3():
    global theta_z
    glPushMatrix()
    glTranslatef(rotation_center[0], rotation_center[1], rotation_center[2])
    glColor3f(0.3, 0.3, 0.3)
    glRotatef(-theta_z, 0, 0, 1)
    glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])

    # Translate to the current position
    glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)

    draw_box(*(0.2, -0.5, 0.8 ), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_3_2(x,y,z):
    global theta_z, translate_x, translate_z
    glPushMatrix()
    # glTranslatef(rotation_center[0], rotation_center[1], rotation_center[2])
    glTranslatef(x,y,z)
    glColor3f(0.3, 0.3, 0.3)
    # glRotatef(-theta_z, 0, 0, 1)
    # glTranslatef(-rotation_center[0], -rotation_center[1], -rotation_center[2])

    # Translate to the current position
    glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)
    glTranslatef(translate_x, translate_y, translate_z)
    draw_box(*(0.2, -1, 0.8 ), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_4():
    global theta_z
    glPushMatrix()
    glTranslatef(rotation_center2[0], rotation_center2[1], rotation_center2[2])
    glColor3f(0.3, 0.3, 0.3)
    glRotatef(theta_z, 0, 0, 1)
    glTranslatef(-rotation_center2[0], -rotation_center2[1], -rotation_center2[2])

    # Translate to the current position
    glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)

    draw_box(*(1.8, -0.5, 0.8 ), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def draw_leg_4_2(x,y,z):
    global theta_z, translate_x, translate_z
    glPushMatrix()
    # glTranslatef(rotation_center2[0], rotation_center2[1], rotation_center2[2])
    glTranslatef(x,y,z)
    glColor3f(0.3, 0.3, 0.3)
    # glRotatef(theta_z, 0, 0, 1)
    # glTranslatef(-rotation_center2[0], -rotation_center2[1], -rotation_center2[2])

    # Translate to the current position
    # glTranslatef(translate_x_rotating, translate_y_rotating, translate_z_rotating)
    # glTranslatef(translate_x, translate_y, translate_z)
    draw_box(*(1.8, -1, 0.8 ), 0.2, 0.5, 0.2)
    

    glPopMatrix()

def handle_mouse_input(event):
    global angle_x, angle_y, mouse_dragging, prev_mouse_pos

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            mouse_dragging = True
            prev_mouse_pos = pygame.mouse.get_pos()

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            mouse_dragging = False

    elif event.type == pygame.MOUSEMOTION and mouse_dragging:
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - prev_mouse_pos[0]
        dy = mouse_pos[1] - prev_mouse_pos[1]

        angle_x = dy * 0.05
        angle_y = dx * 0.05

        prev_mouse_pos = mouse_pos

theta_z=0
rotation_step=1

def main():
    global angle_x, angle_y, theta_y, theta_x, theta_z, rotation_step,translate_x, translate_z
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                handle_mouse_input(event)

        # update the rotation of the leg
        theta_z+=rotation_step

        if theta_z >= 30 or theta_z <= -30:
            rotation_step *= -1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(angle_x, 1, 0, 0)
        glRotatef(angle_y, 0, 1, 0)
        draw_boxy_animal()
        draw_leg_1()
        draw_leg_1_2(x=0.5*math.sin(math.radians(theta_z)),y=0.0,z=0.0)
        draw_leg_2()
        draw_leg_2_2(x=-0.5*math.sin(math.radians(theta_z)),y=0.0,z=0.0)
        draw_leg_3()
        draw_leg_3_2(x=-0.5*math.sin(math.radians(theta_z)),y=0.0,z=0.0)
        draw_leg_4()
        draw_leg_4_2(x=0.5*math.sin(math.radians(theta_z)),y=0.0,z=0.0)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()