import math
import random

import pygame

from car3 import VehicleSprite



pygame.init()
screen = pygame.display.set_mode((800, 800))
rect = screen.get_rect()
clock = pygame.time.Clock()

WHITE = pygame.Color('white')
# Load images globally and reuse them in your program.
# loading the images to improve the performance.
VEHICLE1 = pygame.Surface((40, 70), pygame.SRCALPHA)
VEHICLE1.fill((130, 180, 20))
BACKGROUND = pygame.Surface((1280, 800))
BACKGROUND.fill((30, 30, 30))

bg =  pygame.image.load('track3.png')



class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Background(pygame.sprite.Sprite):

    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)

def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        car = Car(0, 0)
        ppu = 32

def game_loop():
    background = Background(BACKGROUND, [0, 0])
    car = VehicleSprite(VEHICLE1, rect.center)
    car_group = pygame.sprite.Group(car)
    all_sprites = pygame.sprite.Group(car_group)
    
    camera = pygame.math.Vector2(0, 0)
    camera = pygame.math.Vector2(0,0)
    done = False

    car_group = pygame.sprite.Group(car)
    all_sprites = pygame.sprite.Group(car_group)
    global x
    global y
    x = 0
    y = 0
   
    done = False

    while not done:
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                #Car movement
                if event.key == pygame.K_d:
                    car.k_right = -2
                elif event.key == pygame.K_a:
                    car.k_left = 2
                elif event.key == pygame.K_w:
                    car.k_up = 0.1
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
                elif event.key == pygame.K_s:
                    car.k_down = 0
                    
        screen.blit(bg,(x,y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
                # car Input (Player 1)
        if keys[pygame.K_d]:
            car.k_right = -2
            #x -=3
        elif keys[pygame.K_a]:
            car.k_left = 2
            #x += 3
        elif keys[pygame.K_w]:
            y += 3
        elif keys[pygame.K_s]:
                    #car.k_down = -0.1
            y -=3

        if keys[pygame.K_RIGHT]:
                    #car.k_right = -2
            car.k_right = 0
        elif keys[pygame.K_LEFT]:
                    #car.k_left = 2
            car.k_left = 0
        elif keys[pygame.K_UP]:
            car.k_up = 0
        elif keys[pygame.K_DOWN]:
                    #car.k_down = -0.1
            car.k_down = 0

        camera -= car.velocity

      

        all_sprites.update(time)

        
        screen.blit(background.image, background.rect)
        
        #screen.blit(background.image, background.rect)

        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+camera)

        pygame.display.flip()


game_loop()
pygame.quit()
