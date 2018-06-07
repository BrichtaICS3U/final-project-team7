import math
import random


import pygame

from Carclass import Player



pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

WHITE =  (255,255,255)
bg =  pygame.image.load('track4.png')

all_sprites = pygame.sprite.Group()
player = Player(0, 0)
all_sprites.add(player)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Background(pygame.sprite.Sprite):

    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)

def game_loop():
    car_group = pygame.sprite.Group(player)
    all_sprites = pygame.sprite.Group(car_group)

    camera = pygame.math.Vector2(0, 0)

global speed
speed = 5

global x
global y
x = 0
y = 0

done = False

while not done:
    screen.fill(WHITE)
    screen.blit(bg,[x,y])

    print(x,y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rotLeft(7)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rotRight(7)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            x, y, speed = player.accelerate(x, y, speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            x, y,  = player.moveBackward(x, y,)
        else:
            x, y = player.deccelerate(x, y)

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        time = clock.tick(60)


game_loop()

pygame.quit()