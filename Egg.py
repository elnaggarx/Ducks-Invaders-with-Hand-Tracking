from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

import pygame
class Egg:
    
    def __init__(self, startingX, startingY, size):
        self.startingX = startingX
        self.startingY = startingY
        self.size = size




    def __del__(self):
        print("Egg Destroyed")


    def move(self):
        self.startingY-=0.1


    def drawEgg(self):
        quad = gluNewQuadric()
        glPushMatrix()
        glTranslatef(self.startingX, self.startingY - 4 * self.size, 0) 

        glScalef(1.0 * self.size, 1.3 * self.size, 1.0 * self.size) 
        glColor3f(1.0, 0.95, 0.7)
        gluSphere(quad, 1, 32, 32)
        glPopMatrix()




