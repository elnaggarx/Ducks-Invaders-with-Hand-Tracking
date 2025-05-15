import math
from OpenGL.GL import *

class Bullet:
    def __init__(self, x, y, speed=0.2, size=0.01):
        self.x = x
        self.y = y
        self.speed = speed 
        self.size = size    
        self.alive = True   

    def move(self):
        self.y += self.speed
        if self.y > 4:  
            self.alive = False

    def draw(self):
        if not self.alive:
            return

        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size * 3, 1.0)

        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.2)  # bright yellow bullet
        glVertex2f(-0.5,  0.5)
        glVertex2f( 0.5,  0.5)
        glVertex2f( 0.5, -0.5)
        glVertex2f(-0.5, -0.5)
        glEnd()

        glPopMatrix()


    def checkCollisionWithDuck(self,duckX,duckY):
        if self.x+0.01>=duckX-0.075 and self.x-0.01<=duckX+0.075 and self.y+0.03>=duckY-0.21 and self.y-0.03<=duckY+0.21:
            return True

    def __del__(self):
        print("Bullet Destroyed")