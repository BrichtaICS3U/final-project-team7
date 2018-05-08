import pygame
WHITE = (255, 255, 255)
 
class Car(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height, speed, max_steering=40, ,max_acceleration=10.0):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
        self.brake_deceleration = 12
        self.free_deceleration = 10
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering

        self.acceleration = 0.0
        self.steering = 0.0
        
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
