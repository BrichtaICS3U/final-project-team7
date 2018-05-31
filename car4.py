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
 
    def moveBackward(self, x, y):
        if self.speed >= 5:
            self.speed -= 5
            x += math.cos(math.radians(self.angle))*self.speed
            y -= math.sin(math.radians(self.angle))*self.speed
        elif self.speed >= 0:
            self.speed += 5
            x += math.cos(math.radians(self.angle))*self.speed
            y -= math.sin(math.radians(self.angle))*self.speed
        return x, y
    
    def accelerate(self, x, y):
        self.speed += 5
        x -= math.cos(math.radians(self.angle))*self.speed
        y += math.sin(math.radians(self.angle))*self.speed
        return x, y
    
    def deccelerate(self, x, y):
        if self.speed >= 5:
            self.speed *= 0.95
            x -= math.cos(math.radians(self.angle))*self.speed
            y += math.sin(math.radians(self.angle))*self.speed
        elif self.speed >= 0:
            self.speed = 0
            x -= math.cos(math.radians(self.angle))*self.speed
            y += math.sin(math.radians(self.angle))*self.speed
        return(x, y)

    def draw(self, screen):
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        screen.blit(self.image, self.rect)

   
        
