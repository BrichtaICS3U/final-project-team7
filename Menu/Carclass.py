import pygame, math
import random
pygame.init()
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
SCREENWIDTH = 800
SCREENHEIGHT = 800



#class Entity(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        
class Player(pygame.sprite.Sprite):

    def __init__(self, startangle, speed):

        super().__init__()


        self.image = pygame.image.load("download.png")
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
 
    def moveBackward(self, x, y, speed):
        if speed >= 7:
            speed -= 7
            x -= math.cos(math.radians(self.angle))*speed
            y += math.sin(math.radians(self.angle))*speed
        elif speed >= 0:
            speed += 7
            x -= math.cos(math.radians(self.angle))*speed
            y += math.sin(math.radians(self.angle))*speed
        return x, y, speed
    
    def accelerate(self, x, y, speed):
        speed += 1
        x -= math.cos(math.radians(self.angle))*speed
        y += math.sin(math.radians(self.angle))*speed
        return x, y, speed
    
    def deccelerate(self, x, y, speed):
        if speed >= 1:
            speed *= 1
            x -= math.cos(math.radians(self.angle))*speed
            y += math.sin(math.radians(self.angle))*speed
        elif speed >= 0:
            speed = 0
            x -= math.cos(math.radians(self.angle))*speed
            y += math.sin(math.radians(self.angle))*speed
        return x, y, speed

    def draw(self, screen):
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        screen.blit(self.image, self.rect)

   
        
