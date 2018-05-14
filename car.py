import pygame
WHITE = (255, 255, 255)
 
class Car(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height, speed):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
 
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
 
 
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    def rotRight(self):
        self.angle += self.turnRate
        if self.speed == 0:
            self.speed = self.turnRate
        while self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotate(self.original, self.angle)
    def rotLeft(self):
        self.angle -= self.turnRate
        if self.speed == 0:
            self.speed = self.turnRate
        while self.angle > 359:
            self.angle -= 360
        self.image = pygame.transform.rotate(self.original, self.angle)
