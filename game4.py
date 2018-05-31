import math
import random

import pygame

from car4 import Player



pygame.init()
screen = pygame.display.set_mode((800, 800))
rect = screen.get_rect()
clock = pygame.time.Clock()

WHITE =  (255,255,255)
BLUE = (30,144,255)
VEHICLE1 = pygame.Surface((40, 70), pygame.SRCALPHA)
BACKGROUND = pygame.Surface((1280, 800))
bg =  pygame.image.load('track4.png')

all_sprites = pygame.sprite.Group()
player = Player(0,0)
all_sprites.add(player)




class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Background(pygame.sprite.Sprite):

    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)



camera = pygame.math.Vector2(0,0)


global x
global y
x = 0
y = 0
   
done = False

while not done:

    screen.fill(BLUE)
    screen.blit(bg,(x,y))

    for event in pygame.event.get():
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rotLeft(10)          
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rotRight(10)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            x, y = player.accelerate(x, y)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            x, y = player.moveBackward(x, y)
        else:
            x, y = player.deccelerate(x, y)
       
      
       
    all_sprites.update()
    all_sprites.draw(screen)
    
        


        
    pygame.display.flip()
    time = clock.tick(60)


game_loop()
pygame.quit()
