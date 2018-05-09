import pygame, random
from car import Car
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



carryOn = True
clock=pygame.time.Clock()

        #Game Logic
for car in all_coming_cars:
    car.moveForward(speed)
    if car.rect.y > SCREENHEIGHT:
        car.changeSpeed(random.randint(50,100))
        car.repaint(random.choice(colorList))
        car.rect.y = -200

        all_sprites_list.update()

        #Background Screen
        screen.fill(GREEN)
        #Road
        pygame.draw.ellipse(screen, GREY, [40,0, 400,SCREENHEIGHT])
        
        
        
        
        all_sprites_list.draw(screen)

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per second
        clock.tick(60)

#Check if there is a car collision
        car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
        for car in car_collision_list:
            print("Car crash!")
            carryOn=False

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Sounds/soundtrack.mp3')
pygame.mixer.music.play(0)

pygame.quit()
