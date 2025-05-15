from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import pygame 


class Spaceship:


    def __init__(self, startingX, startingY, size):
        self.startingX = startingX
        self.startingY = startingY
        self.size = size
        self.boom_sound = pygame.mixer.Sound("assets/sounds/boom.mp3") 




    def draw_spaceship(self,moveX):
        self.moveX = moveX
        glPushMatrix()
        glTranslatef(moveX, self.startingY, 0)
        glScalef(self.size, self.size, 1)


    # === Sleek, Aggressive Fuselage (Updated Middle Part) ===
        glBegin(GL_POLYGON)
        glColor3f(0.95, 0.95, 1.0)   # Tip highlight
        glVertex2f(0, 50)            # Nose tip

        glColor3f(0.6, 0.6, 0.8)
        glVertex2f(6, 35)

        glColor3f(0.4, 0.4, 0.6)
        glVertex2f(10, 10)

        glColor3f(0.3, 0.3, 0.5)
        glVertex2f(14, -15)

        glColor3f(0.2, 0.2, 0.4)
        glVertex2f(8, -38)

        glColor3f(0.2, 0.2, 0.4)
        glVertex2f(-8, -38)

        glColor3f(0.3, 0.3, 0.5)
        glVertex2f(-14, -15)

        glColor3f(0.4, 0.4, 0.6)
        glVertex2f(-10, 10)

        glColor3f(0.6, 0.6, 0.8)
        glVertex2f(-6, 35)
        glEnd()

        # === Split Nose Prongs ===
        glBegin(GL_TRIANGLES)
        glColor3f(0.8, 0.8, 1.0)
        glVertex2f(0, 50)
        glColor3f(0.3, 0.3, 0.6)
        glVertex2f(4, 40)
        glVertex2f(0, 42)

        glVertex2f(0, 50)
        glVertex2f(-4, 40)
        glVertex2f(0, 42)
        glEnd()

        # === Wings with Shading ===
        glBegin(GL_TRIANGLES)
        glColor3f(0.1, 0.1, 0.6)  # Dark base
        glVertex2f(-8, 10)
        glColor3f(0.3, 0.3, 0.9)  # Wing tip
        glVertex2f(-35, -10)
        glColor3f(0.2, 0.2, 0.7)
        glVertex2f(-5, -5)

        glColor3f(0.1, 0.1, 0.6)
        glVertex2f(8, 10)
        glColor3f(0.3, 0.3, 0.9)
        glVertex2f(35, -10)
        glColor3f(0.2, 0.2, 0.7)
        glVertex2f(5, -5)
        glEnd()

        # === Cockpit Dome with Gloss Gradient ===
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 0.3, 0.3)  # Core red
        glVertex2f(0, 25)
        for angle in range(0, 361, 30):
            rad = math.radians(angle)
            if angle < 180:
                glColor3f(0.8, 0.2, 0.2)  # Highlight side
            else:
                glColor3f(0.4, 0.05, 0.05)  # Shadowed side
            glVertex2f(math.cos(rad) * 6, 25 + math.sin(rad) * 5)
        glEnd()

        # === Afterburners with Metallic Gradient ===
        glBegin(GL_QUADS)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(-16, -30)
        glColor3f(0.2, 0.2, 0.2)
        glVertex2f(-10, -30)
        glVertex2f(-10, -42)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(-16, -42)

        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(10, -30)
        glColor3f(0.2, 0.2, 0.2)
        glVertex2f(16, -30)
        glVertex2f(16, -42)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(10, -42)
        glEnd()

        # === Engine Flames with Gradient Flicker ===
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.8, 0.0)
        glVertex2f(-13, -42)
        glColor3f(1.0, 0.4, 0.0)
        glVertex2f(-10.5, -42)
        glColor3f(1.0, 0.2, 0.0)
        glVertex2f(-11.75, -52)

        glColor3f(1.0, 0.8, 0.0)
        glVertex2f(10.5, -42)
        glColor3f(1.0, 0.4, 0.0)
        glVertex2f(13, -42)
        glColor3f(1.0, 0.2, 0.0)
        glVertex2f(11.75, -52)
        glEnd()

        glPopMatrix()


    def checkCollisionWithEgg(self,eggX , eggY):
        if self.moveX-0.126<=eggX+0.07 and self.moveX+0.126>=eggX-0.07 and self.startingY+0.45>= eggY-0.091 and self.startingY-0.45<=eggY+0.091:
            self.boom.play()
            return True
