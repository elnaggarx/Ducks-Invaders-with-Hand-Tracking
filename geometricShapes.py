from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

class Cube:

    def __init__(self):
        self.vertecies = [
        (1,-1,-1),
        (1,1,-1),
        (-1,1,-1),
        (-1,-1,-1),
        (1,-1,1),
        (1,1,1),
        (-1,-1,1),
        (-1,1,1)
        ]
        self.edges = [
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7),

        ]

        self.faces = [
            (0,1,2,3),
            (3,2,7,6),
            (6,7,5,4),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6)
        ]
    
    def drawCube(self,colors):
    
        glBegin(GL_QUADS)
        
        for face in self.faces:
            x=0
            for vertex in face:
                glColor3fv(colors[x])
                x=x+1
                glVertex3fv(self.vertecies[vertex])
        glEnd()


def draw_circle( r , segments , color):
    glColor3fv(color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)  # center point of the fan
    
    for i in range(segments + 1):
        angle = 2 * pi * i / segments
        x =  r * cos(angle)
        y =  r * sin(angle)
        glVertex3f(x, y, 0)
    glEnd()
 
 
def draw_point(x,y):
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex3f(x,y,-10)
    glEnd()


