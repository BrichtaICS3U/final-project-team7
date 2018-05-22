
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

import pygame, random
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (244, 164, 66)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)


SCREENWIDTH=800
SCREENHEIGHT=800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

all_sprites_list = pygame.sprite.Group()

playerCar = Car(ORANGE, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100

carryOn = True
clock=pygame.time.Clock()
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     playerCar.moveRight(10)
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
                playerCar.moveLeft(5)
        if keys[pygame.K_d]:
                playerCar.moveRight(5)
        if keys[pygame.K_a]:
                speed += 0.05
        if keys[pygame.K_s]:
                speed -= 0.05
        #Game Logic

screen.fill(GREEN)


all_sprites_list.add(playerCar)

        #Background Screen
pygame.draw.rect(screen, GREY, [40,0, 400,SCREENHEIGHT])
        
pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)

pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
      
pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)
        
        
all_sprites_list.draw(screen)

        #Refresh Screen
pygame.display.flip()

        #Number of frames per second
clock.tick(60)

        #Road
pygame.draw.ellipse(screen, GREY, [40,0, 400,SCREENHEIGHT])
        
all_sprites_list.draw(screen)

        #Refresh Screen
pygame.display.flip()

        #Number of frames per second
clock.tick(60)

#Check if there is a car collision
car_collision_list = pygame.sprite.spritecollide(playerCar,enemylist,False)
for car in car_collision_list:
    print("Car crash!")
    carryOn=False

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Sounds/soundtrack.mp3')
pygame.mixer.music.play(0)

pygame.quit()

