import math
import random

import pygame

from car import VehicleSprite



pygame.init()
screen = pygame.display.set_mode((800, 800))
rect = screen.get_rect()
clock = pygame.time.Clock()

# Load images globally and reuse them in your program.
# Also use the `.convert()` or `.convert_alpha()` methods after
# loading the images to improve the performance.
VEHICLE1 = pygame.Surface((40, 70), pygame.SRCALPHA)
VEHICLE1.fill((130, 180, 20))
BACKGROUND = pygame.Surface((1280, 800))
bg =  pygame.image.load('track3.png')


def update(self, time):
        # SIMULATION
        self.speed += self.k_up + self.k_down
        # To clamp the speed.
        self.speed = max(-self.MAX_REVERSE_SPEED,
                         min(self.speed, self.MAX_FORWARD_SPEED))

        # Degrees sprite is facing (direction)
        self.direction += (self.k_right + self.k_left)
        rad = math.radians(self.direction)
        self.velocity.x = -self.speed*math.sin(rad)
        self.velocity.y = -self.speed*math.cos(rad)
        self.position += self.velocity
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect(center=self.position)


class Background(pygame.sprite.Sprite):

    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)


def game_loop():
    background = Background(BACKGROUND, [0, 0])
    car = VehicleSprite(VEHICLE1, rect.center)
    

    car_group = pygame.sprite.Group(car)
    all_sprites = pygame.sprite.Group(car_group)

   
    done = False

    while not done:
        time = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # car Input (Player 1)
                if event.key == pygame.K_d:
                    car.k_right = -2
                elif event.key == pygame.K_a:
                    car.k_left = 2
                elif event.key == pygame.K_w:
                    car.k_up = 0.8
                elif event.key == pygame.K_s:
                    car.k_down = -0.1

                elif event.key == pygame.K_ESCAPE:
                    done = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    car.k_right = 0
                elif event.key == pygame.K_a:
                    car.k_left = 0
                elif event.key == pygame.K_w:
                    car.k_up = 0
                elif event.key == pygame.K_d:
                    car.k_down = 0

    

        all_sprites.update(time)
        
        screen.blit(bg,(0,0))
        

        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft)

        pygame.display.flip()


game_loop()
pygame.quit()
