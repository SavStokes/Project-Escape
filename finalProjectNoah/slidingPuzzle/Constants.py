#####################################################################
#   File containing constants that you might need in your assignment.
#   Make sure to import the library in all your files using a statement
#   like:
#   from Constants import *
#####################################################################

# import libraries that you will need
import pygame
from random import randint, choice
from Item import *


# constants for screen size
WIDTH = 1000
HEIGHT = 800

PLAYERLENGTH = 10

WALLWIDTH = (WIDTH - 300)/2
WALLLENGTH = (HEIGHT - 300)/2
#constants for color
WHITE = [0xD6, 0xD6, 0xD6]
MAGENTA = [0xD6,0x47,0xD6]
CYAN = [0x47,0xD6,0xD6]
BLACK = [0x00,0x00,0x00]
YELLOW = [0xD6,0xD6,0x47]

COLORS = [WHITE, MAGENTA, CYAN, BLACK, YELLOW]

#Timer for update
UTIMER = 0.002

# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)
