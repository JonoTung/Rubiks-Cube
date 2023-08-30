import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective
from utils import *

edges = [
    (0, 1), (0, 3), (0, 4), (2, 1),
    (2, 3), (2, 7), (6, 3), (6, 4),
    (6, 7), (5, 1), (5, 4), (5, 7)
]

colors = [
    (0.5647, 0.9333, 0.5647), # green
    (1, 0.9333, 0.5647), # yellow
    (1, 0.5647, 0.5647), #red
    (1, 0.8, 0.5647), # orange
    (0.5647, 0.8, 1), # blue
    (1, 1, 1), # white
]

faces = {
    Face.B: [0, 1, 2, 3],  # Back face
    Face.L: [3, 2, 7, 6],  # Left face
    Face.F: [5, 4, 6, 7],  # Front face
    Face.R: [0, 1, 5, 4],  # Right face
    Face.U: [2, 1, 5, 7],  # Top face
    Face.D: [3, 0, 4, 6]   # Bottom face
}

initial_colors = {
    Face.U: Color.WHITE,
    Face.F: Color.GREEN,
    Face.R: Color.RED,
    Face.D: Color.YELLOW,
    Face.B: Color.BLUE,
    Face.L: Color.ORANGE,
}

def draw_cube(coordinate, edge_length):
    x = (coordinate[0] - edge_length) * edge_length * 2
    y = (coordinate[1] - edge_length) * edge_length * 2
    z = (coordinate[2] - edge_length) * edge_length * 2
    vertices = [
        (x + edge_length, y - edge_length, z - edge_length),
        (x + edge_length, y + edge_length, z - edge_length),
        (x - edge_length, y + edge_length, z - edge_length),
        (x - edge_length, y - edge_length, z - edge_length),
        (x + edge_length, y - edge_length, z + edge_length),
        (x + edge_length, y + edge_length, z + edge_length),
        (x - edge_length, y - edge_length, z + edge_length),
        (x - edge_length, y + edge_length, z + edge_length)
    ]
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv(initial_colors[face].value)
        for vertex in faces[face]:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set up perspective projection
    field_of_view = 50.0
    near_plane = 0.1
    far_plane = 100.0
    gluPerspective(field_of_view, (display[0] / display[1]), near_plane, far_plane)

    glTranslatef(0.0, 0.0, -15)
    glRotatef(40, 1, 1, 0)
    glEnable(GL_DEPTH_TEST)
    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        edge_length = 1
        for x in range(0, 3):
            for y in range(0, 3):
                for z in range(0, 3):
                    # if x == 0:
                    #     glPushMatrix()
                    #     glRotatef(rotation_angle, 1, 0, 0)  # Rotate only along the X-axis
                    #     draw_cube((x, y, z), edge_length)
                    #     glPopMatrix()
                    # if x == 1:
                    #     glPushMatrix()
                    #     glRotatef(rotation_angle, 1, 0, 0)  # Rotate only along the X-axis
                    #     draw_cube((x, y, z), edge_length)
                    #     glPopMatrix()
                    # if x == 2:
                    #     glPushMatrix()
                    #     glRotatef(rotation_angle, 1, 0, 0)  # Rotate only along the X-axis
                    #     draw_cube((x, y, z), edge_length)
                    #     glPopMatrix()
                    # if y == 0:
                    #     glPushMatrix()
                    #     glRotatef(rotation_angle, 0, 1, 0)  # Rotate only along the X-axis
                    #     draw_cube((x, y, z), edge_length)
                    #     glPopMatrix()
                    # else:
                        glPushMatrix()
                        glRotatef(rotation_angle, 0, 1, 0)
                        draw_cube((x, y, z), edge_length)
                        glPopMatrix()
                    # draw_cube((x, y, z), edge_length)
        rotation_angle += 1
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
