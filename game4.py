import math
import random


import pygame

from car4 import Player



pygame.init()
screen = pygame.display.set_mode((800, 800))
rect = screen.get_rect()
clock = pygame.time.Clock()

WHITE =  (255,255,255)
# Load images globally and reuse them in your program.
# loading the images to improve the performance.
VEHICLE1 = pygame.Surface((40, 70), pygame.SRCALPHA)
VEHICLE1.fill((130, 180, 20))
BACKGROUND = pygame.Surface((1280, 800))
bg =  pygame.image.load('track4.png')

all_sprites = pygame.sprite.Group()
player = Player(0, 0)
all_sprites.add(player)

#car = Car(0,0)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Background(pygame.sprite.Sprite):

    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)



camera = pygame.math.Vector2(0,0)

global speed
speed = 5
   

#car_group = pygame.sprite.Group(car)
#all_sprites = pygame.sprite.Group(car_group)
global x
global y
x = 0
y = 0
   
done = False

while not done:
    screen.fill(WHITE)
    screen.blit(bg,(x,y))
    time = clock.tick(60)
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rotLeft(10)          
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rotRight(10)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           x, y, speed = player.accelerate(x, y, speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            x, y, speed = player.moveBackward(x, y, speed)
        else:
            x, y, speed = player.deccelerate(x, y, speed)
       
      
       
            

    #camera -= player.velocity
    all_sprites.update(time)
    all_sprites.draw(screen)
    
        #screen.blit(background.image, background.rect)


    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect.topleft)
        
    pygame.display.flip()


game_loop()
pygame.quit()
