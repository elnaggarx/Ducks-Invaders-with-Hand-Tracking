from geometricShapes import *
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame as pg
import random
from Egg import *


class Duck():

    def __init__(self,size,startingX,startingY):
        self.size = size
        self.startingX = startingX
        self.startingY = startingY
        self.bodyColors = [
        (1.0, 1.0, 0.8), 
        (1.0, 1.0, 0.6), 
        (1.0, 0.95, 0.4),
        (1.0, 0.85, 0.2), 
        (1.0, 0.75, 0.0), 
        (0.95, 0.65, 0.0), 
        (0.90, 0.55, 0.0), 
        (0.85, 0.45, 0.0) 
        ]
        self.legsColors= [
            (0.6, 0.2, 0.0),  # dark reddish orange
            (0.8, 0.3, 0.0),
            (1.0, 0.4, 0.0),
            (1.0, 0.5, 0.0),  # pure orange
            (1.0, 0.6, 0.2),
            (1.0, 0.7, 0.4),  # light orange
        ]
        self.next_egg_drop_time = pygame.time.get_ticks() + random.randint(1000, 5000)

        self.egg_sound = pygame.mixer.Sound("assets/sounds/egggDrop.mp3") 

  

    def dropEgg(self, current_time):
        if current_time >= self.next_egg_drop_time:
            self.next_egg_drop_time = current_time + random.randint(1000, 5000)
            self.egg_sound.play()
            return Egg(self.startingX , self.startingY  ,0.07 )

    




    def drawDuck(self):

        glPushMatrix()
        glTranslatef(self.startingX,self.startingY,0)
        
        glScalef(self.size,self.size,self.size)
        #Body
        glPushMatrix()
        glScalef(0.4,0.4,0.4)
        glRotatef(10,0,1,0)
        Cube().drawCube(self.bodyColors)
        glPopMatrix()
        
        #Head
        glPushMatrix()
        glDisable(GL_BLEND)
        glRotatef(10,0,1,0)
        glTranslatef(0,0.7,0)
        glScalef(0.3,0.3,0.3)
        Cube().drawCube(self.bodyColors)
        glPopMatrix()

        #Right Leg
        glPushMatrix()
        glTranslatef(0.2,-0.53,0)
        glRotatef(10,0,1,0)
        glScalef(0.1,0.1,0.1)
        Cube().drawCube(self.legsColors)
        glPopMatrix()

        #Left Leg
        glPushMatrix()
        glTranslatef(-0.2,-0.53,0)
        glRotatef(10,0,1,0)
        glScalef(0.1,0.1,0.1)
        Cube().drawCube(self.legsColors)
        glPopMatrix()

        #Left Eye
        glPushMatrix()
        glTranslatef(-0.13,0.75,0.31)
        glRotatef(10,0,1,0)
        draw_circle(0.1,32,(1,1,1))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.13,0.75,0.31)
        glRotatef(10,0,1,0)
        draw_circle(0.07,32,(0,0,0))
        glPopMatrix()

        #Right Eye
        glPushMatrix()
        glTranslatef(0.15,0.75,0.31)
        glRotatef(10,0,1,0)
        draw_circle(0.1,32,(1,1,1))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.15,0.75,0.31)
        glRotatef(10,0,1,0)
        draw_circle(0.07,32,(0,0,0))
        glPopMatrix()

        #Beak
        glPushMatrix()
        glRotatef(10,0,1,0)
        glTranslatef(0,0.6,0.33)
        glScalef(0.1,0.1,0.1)
        beakCube = Cube()
        beakCube.drawCube(self.legsColors)
        glPopMatrix()

        glPopMatrix()

    def __del__(self):
        print("Duck Killed")