# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame, random

from car import Car
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (25, 142, 7)
RED = (186, 22, 22)
BLUE = (82, 210, 216)
YELLOW = (238, 255, 0)
GREY = (140, 138, 130)

speed = 1
colorList = (RED, BLACK, BLUE, WHITE, YELLOW)

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("car race")

#This will be a list that will contain all the spriteswe intend to use in this game.
all_sprites_list = pygame.sprite.Group()

playerCar = Car(YELLOW, 60,80,20)
playerCar.rect.x = 160
playerCar.rect.y =500

car1 = Car(RED, 90, 80, random.randint(50,100))
car1.rect.x = 60
car1.rect.y =-600

car2 = Car(BLACK, 60, 80, random.randint(50,100))
car2.rect.x = 160
car2.rect.y = -600

car3 = Car(BLUE, 60, 80, random.randint(50,100))
car3.rect.x = 260
car3.rect.y = -300

car4 = Car(WHITE, 60, 80, random.randint(50,100))
car4.rect.x = 360
car4.rect.y = -900

all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)


# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playerCar.moveRight(10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerCar.moveLeft(5)
    if keys[pygame.K_d]:
        playerCar.moveRight(5)
    if keys[pygame.K_w]:
        speed += 0.05
    if keys[pygame.K_s]:
        speed -= 0.05
                    

    # --- Game logic goes here
    car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
    for car in car_collision_list:
        print("Car Crash!")
        carryOn = False
        
    for car in all_coming_cars:
        car.moveUp(speed)
        if car.rect.y > 600:
            car.changeSpeed(random.randint(50,100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200
            
    all_sprites_list.update()
   
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(GREY)

    # Queue different shapes and lines to be drawn
    pygame.draw.rect(screen, BLACK, [40, 0, 400, 600],5)
    pygame.draw.line(screen, WHITE, [140,0],[140,600],5)
    pygame.draw.line(screen, WHITE, [240,0],[240,600],5)
    pygame.draw.line(screen, WHITE, [340,0],[340,600],5)

    #Draw all sprites in one go.(only have one at the moment                      
    all_sprites_list.draw(screen)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
