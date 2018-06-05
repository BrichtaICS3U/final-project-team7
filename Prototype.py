import math
import random

import pygame

from car4 import Player
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
    car = Player(VEHICLE1, rect.center)
    car_group = pygame.sprite.Group(car)
    all_sprites = pygame.sprite.Group(car_group)
    
    camera = pygame.math.Vector2(0, 0)
    done = False

    while not done:
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    player.rotLeft(7)
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    player.rotRight(7)
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    x, y = player.accelerate(x, y)
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                     x, y,  = player.moveBackward(x, y,)
                else:
                     x, y = player.deccelerate(x, y)


      

        all_sprites.update(time)

        
        screen.blit(background.image, background.rect)

        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+camera)

        pygame.display.flip()


game_loop()
pygame.quit()
