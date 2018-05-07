# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()


BackGround = pygame.image.load('BACKgROUNd reaL.jpg')

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
            self.bg = WHITE # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_play_function():
    global level
    level += 1

def my_sound_function():
    print('Sound')


def my_settings_function():
    """A function that advances to settings shell"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

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

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_Play = Button('Play', (SCREENWIDTH/12, SCREENHEIGHT/8),my_play_function, bg=(BLUE), fg = (WHITE))
button_Previous = Button("Return", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_previous_function, bg=(WHITE))
button_Quit = Button("Quit", (SCREENWIDTH/12, SCREENHEIGHT*2/3), my_quit_function, bg=(WHITE))
button_Settings = Button("Settings", (SCREENWIDTH/12, SCREENHEIGHT/2),my_settings_function, bg=(BLUE))
button_Sound = Button("Sound", (SCREENWIDTH/2, SCREENHEIGHT/4), my_sound_function, bg=(WHITE))
button_On = Button("ON", (SCREENWIDTH/4, SCREENHEIGHT/3), my_on_function, bg=(WHITE))
button_Off = Button("OFF", (SCREENWIDTH*3/4, SCREENHEIGHT/3), my_off_function, bg=(WHITE))
#arrange button groups depending on level
level1_buttons = [button_Settings, button_Play, button_Quit]
level2_buttons = [button_Sound, button_Previous,button_On, button_Off]

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)
    screen.blit(BackGround,(0,0))
    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('comicsansms',42)
        text = font.render('Auto Racing II',1, WHITE)
        screen.blit(text, (300,1))
    elif level == 2:
        for button in level2_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

