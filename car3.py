import pygame
import math
import random

SCREENWIDTH = 800
SCREENHEIGHT = 800

#class Entity(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        
class Player(pygame.sprite.Sprite):

    def __init__(self, startangle, speed):

        super().__init__()

        self.image = pygame.image.load("download.jpg")
        self.original = self.image
        self.angle = startangle
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        self.speed = speed

    def rotRight(self, angle):
        self.angle -= angle
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
 
    def rotLeft(self, angle):
        self.angle += angle
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
 
    #def moveForward(self, bx, by):
        #bx -= math.cos(math.radians(self.angle))*20
       # by += math.sin(math.radians(self.angle))*20
        #return bx, by
 
    def moveBackward(self, bx, by, speed):
        if speed >= 5:
            speed -= 5
            bx += math.cos(math.radians(self.angle))*speed
            by -= math.sin(math.radians(self.angle))*speed
        elif speed >= 0:
            speed +=5
            bx += math.cos(math.radians(self.angle))*speed
            by -= math.sin(math.radians(self.angle))*speed
        return bx, by, speed
    
    def accelerate(self, bx, by, speed):
        speed +=5
        bx -= math.cos(math.radians(self.angle))*speed
        by += math.sin(math.radians(self.angle))*speed
        return bx, by, speed
    
    def deccelerate(self, bx, by, speed):
        if speed >= 5:
            speed *= 0.95
            bx -= math.cos(math.radians(self.angle))*speed
            by += math.sin(math.radians(self.angle))*speed
        elif speed >= 0:
            speed = 0
            bx -= math.cos(math.radians(self.angle))*speed
            by += math.sin(math.radians(self.angle))*speed
        return(bx, by, speed)

   
        
