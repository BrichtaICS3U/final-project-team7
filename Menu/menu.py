import pygame, sys, time
pygame.init()
from Carclass import Player


bg = pygame.image.load('BACKgROUNd reaL.jpg')
BackGround = pygame.image.load('BACKgROUNd reaL.jpg')
background = pygame.image.load('Level 3 BG.jpg')


# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (57, 65, 190)
NEON = (70, 255, 191)
VIOLET = (127, 0, 255)
BLOOD  = (255, 115, 60)
PINK = (255, 96, 210)
TURQ = (70, 77, 219)

SCREENWIDTH = 800
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Black Panther - Trailer Song (Vince Staples - BagBak).mp3')
pygame.mixer.music.play(-1)
class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=RED, fg=BLACK, size=(150, 50), font_name="comic sans ms", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont('freesansbold.ttf', 25)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = BLUE # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()




def my_play_function():
    global level
    level += 2

def my_continue_function():
    global level
    if level == 3:
        level += 1


def my_settings_function():
    """A function that advances to settings shell"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_Previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 2
    
def my_on_function():
    global level
    #pygame.mixer.unpause()
    print("Sound On")

def my_off_function():
    global level
    #pygame.mixer.pause()
    print("Sound Off")

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_Play = Button('Play', (SCREENWIDTH/12, SCREENHEIGHT/8),my_play_function, bg=(WHITE), fg = (BLACK))
button_Previous = Button("TReturn", (SCREENWIDTH/2, SCREENHEIGHT*10/11), my_previous_function, bg=(WHITE))
button_previous = Button("Return", (SCREENWIDTH/2, SCREENHEIGHT*9/11), my_Previous_function, bg=(WHITE))
button_Quit = Button("Quit", (SCREENWIDTH*6/7, SCREENHEIGHT*10/11), my_quit_function, bg =(WHITE))
button_Settings = Button("Settings", (SCREENWIDTH/12, SCREENHEIGHT/4),my_settings_function, bg=(WHITE))
button_On = Button("ON", (SCREENWIDTH/4, SCREENHEIGHT/3), my_on_function, bg=(WHITE))
button_Off = Button("OFF", (SCREENWIDTH*3/4, SCREENHEIGHT/3), my_off_function, bg=(WHITE))
button_Continue = Button('Continue',(SCREENWIDTH/2, SCREENHEIGHT*10/11), my_continue_function, bg = (WHITE))
#arrange button groups depending on level
level1_buttons = [button_Settings, button_Play, button_Quit]
level2_buttons = [button_Previous,button_On, button_Off]
level3_buttons = [button_Continue, button_previous]


#---------Main Program Loop----------
while carryOn:
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)




    screen.fill(WHITE)
    screen.blit(bg,(0,0))
    if level == 1:
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('alternategothic',42)
        text = font.render('Auto Racing II',1, WHITE)
        screen.blit(text, (275,20))

    elif level == 2:
        screen.blit(background,(x,y))
        for button in level2_buttons:
            button.draw()
        font = pygame.font.SysFont('alternategothic',30)
        text = font.render('Sound',1, WHITE)
        screen.blit(text, (368, 195))

    elif level == 3:
        screen.blit(background,(0,0))
        for button in level3_buttons:
            button.draw()
            font = pygame.font.SysFont('alternategothic',30)
        text = font.render ('Speed through the streets while trying to record the',1, WHITE)
        screen.blit(text, (150,110))
        text = font.render ('best time possible! Remember to stay on the road.',1, WHITE)
        screen.blit(text,(150,130))
        text = font.render ('Use arrow keys to control or WASD to control car',1,WHITE)
        screen.blit(text,(150,180))


    elif level == 4:
        import math
        import random
        import pygame
        

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
            
            global x
            global y

            global speed
            speed = 10

            x = 0
            y = 0
            done = False

            while not done:
                screen.fill(WHITE)
                screen.blit(bg,[0,0])

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                        player.rotLeft(7)
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        player.rotRight(7)
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        player.accelerate(x,y,speed)
                    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                        player.moveBackward(x,y,speed)
                   

                    all_sprites.update()
                    all_sprites.draw(screen)
        
                    pygame.display.flip()
                    


        game_loop()
        pygame.quit()
        


# Update the screen with queued shapes
    pygame.display.flip()
    clock.tick(60)

   
pygame.quit()

