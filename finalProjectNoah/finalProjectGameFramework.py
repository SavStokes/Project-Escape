##########################################################
#Noah Folse
#start: 3 April 2024
#Final Project Game Framework *Code Subject to change as program specifics become known
##########################################################
import pygame
from time import sleep
from Item import *
from Constants import *

#class of movable objects directly controlled by the player(DirConMoveable=Direct Control Movable)
class DirConMoveable(pygame.sprite.Sprite,Item):
    
    def __init__(self):
        super().__init__()
        super(pygame.sprite.Sprite,self).__init__()
        surf=pygame.Surface((10,10))
        self.surf = surf
        
    def update(self, pressedKeys):
        if pressedKeys[K_UP]:
            self.goUp()
            sleep(UTIMER)
        elif pressedKeys[K_DOWN]:
            self.goDown()
            sleep(UTIMER)
        elif pressedKeys[K_LEFT]:
            self.goLeft()
            sleep(UTIMER)
        elif pressedKeys[K_RIGHT]:
            self.goRight()
            sleep(UTIMER)
    #calculates the position to display the object
    def getPosition(self):
        spriteX = self.x - (self.size/2)
        spriteY = self.y - (self.size/2)
        return (spriteX, spriteY)

######################################
#MAIN: For testing purposes
######################################

#initialize pygame and display
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#create a Controlable Object
o = DirConMoveable()
RUNNING = True

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(o)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    o.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(o.surf, o.getPosition())
    pygame.display.flip()
