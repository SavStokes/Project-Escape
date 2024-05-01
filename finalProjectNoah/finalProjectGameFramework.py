##########################################################
#Noah Folse
#start: 3 April 2024
#Final Project Game Framework *Code Subject to change as program specifics become known
##########################################################
import pygame
from time import sleep
from Item import *
from Constants import *

DEBUG = False

#class of movable objects directly controlled by the player(DirConMoveable=Direct Control Movable)
class DirConMoveable(pygame.sprite.Sprite,Item):
    
    def __init__(self):
        super().__init__()
        super(pygame.sprite.Sprite,self).__init__()
        surf=pygame.Surface((self.sizeX,self.sizeY))
        self.surf = surf
        self.rect = self.surf.get_rect()
        print(self.rect)

    def moveRect(self,x,y):
        self.rect = self.pygame.rect.move(x,y)
        
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

class Immoveable(pygame.sprite.Sprite,Item):
    
    def __init__(self, name, sizeX, sizeY):
        super().__init__()
        super(pygame.sprite.Sprite,self).__init__(name,sizeX,sizeY)
        surf=pygame.Surface((self.sizeX,self.sizeY))
        self.surf = surf
        self.rect = self.surf.get_rect()

    def wallBlit(self):
        screen.blit(self.surf, self.rect)

class Box():
    # Box requires a name and the coordinates of the top left corner
    def __init__(self, name, color, topLeftX, topLeftY, bottomRightX, bottomRightY):
        self.name = name
        self.color = color
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY
        self.lengthX = (self.bottomRightX - self.topLeftX) - 4 
        self.lengthY = (self.bottomRightY - self.topLeftY) - 4
        
        #box left
        self.boxLeft = Immoveable(self.name+"Left",2,self.lengthY)
        self.boxLeft.rect = self.boxLeft.surf.get_rect()
        self.boxLeft.rect.move_ip(self.topLeftX,self.topLeftY+2)
        self.boxLeft.surf.fill(self.color)
        rightWalls.add(self.boxLeft)

        #box top
        self.boxTop = Immoveable(self.name+"Top",self.lengthX,2)
        self.boxTop.rect = self.boxTop.surf.get_rect() 
        self.boxTop.rect.move_ip(topLeftX+2,topLeftY)
        self.boxTop.surf.fill(self.color)
        downWalls.add(self.boxTop)

        
        #box right
        self.boxRight = Immoveable(self.name+"Right",2,self.lengthY)
        self.boxRight.rect = self.boxRight.surf.get_rect() 
        self.boxRight.rect.move_ip(self.topLeftX + self.lengthX+2,self.topLeftY+2)
        self.boxRight.surf.fill(self.color)
        leftWalls.add(self.boxRight)

        #box down
        self.boxDown = Immoveable(self.name+"Down",self.lengthX,2)
        self.boxDown.rect = self.boxDown.surf.get_rect() 
        self.boxDown.rect.move_ip(self.topLeftX+2,self.topLeftY + self.lengthY+2)
        self.boxDown.surf.fill(self.color)
        upWalls.add(self.boxDown)

        #boxMiddle
        self.boxCenter = Immoveable(self.name+"Center",self.lengthX+4,self.lengthY+4)
        self.boxCenter.rect = self.boxCenter.surf.get_rect()
        self.boxCenter.rect.move_ip(topLeftX,topLeftY)
        self.boxCenter.surf.fill(self.color)


    def boxBlit(self):
        screen.blit(self.boxLeft.surf,self.boxLeft.rect)
        screen.blit(self.boxTop.surf,self.boxTop.rect)
        screen.blit(self.boxRight.surf,self.boxRight.rect)
        screen.blit(self.boxDown.surf,self.boxDown.rect)
        screen.blit(self.boxCenter.surf, self.boxCenter.rect)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, newName):
        if len(newName) > 1:
            self._name = newName
        else:
            self._name = "player 1"
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, newColor):
        for color in COLORS:
            if newColor == color:
                self._color = newColor
            else:
                self._color = CYAN
    # Top Left corner
    @property
    def topLeftX(self):
        return self._topLeftX
    @topLeftX.setter
    def topLeftX(self, newSize):
        if newSize >= 1:
            self._topLeftX = newSize
        else:
            self._topLeftX = self.topLeftX
    @property
    def topLeftY(self):
        return self._topLeftY
    @topLeftY.setter
    def topLeftY(self, newSize):
        if newSize >= 1:
            self._topLeftY = newSize
        else:
            self._topLeftY = self.topLeftY
    # Bottom Right corner
    @property
    def bottomRightX(self):
        return self._bottomRightX
    @bottomRightX.setter
    def bottomRightX(self, newSize):
        if newSize >= 1:
            self._bottomRightX = newSize
        else:
            self._bottomRightX = self.bottomRightX
    @property
    def bottomRightY(self):
        return self._bottomRightY
    @bottomRightY.setter
    def bottomRightY(self, newSize):
        if newSize >= 1:
            self._bottomRightY = newSize
        else:
            self._bottomRightY = self.bottomRightY
    

######################################
#MAIN: For testing purposes
######################################

# initialize pygame and display
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# create a Controlable Object
p = DirConMoveable()

# collision groups
leftWalls = pygame.sprite.Group()
upWalls = pygame.sprite.Group()
rightWalls = pygame.sprite.Group()
downWalls = pygame.sprite.Group()

# create a wall (left)
w1 = Immoveable("wall 1",WALLWIDTH,HEIGHT)
w1.surf.fill(MAGENTA)
leftWalls.add(w1)

# create a wall (up)
w2 = Immoveable("wall 2",WIDTH,WALLLENGTH)
w2.surf.fill(MAGENTA)
upWalls.add(w2)

# create a wall (right)
w3 = Immoveable("wall 3",WALLWIDTH,HEIGHT)
w3.rect.move_ip(WIDTH-WALLWIDTH,0)
w3.surf.fill(MAGENTA)
rightWalls.add(w3)

# create a wall (down)
w4 = Immoveable("wall 4",WIDTH,WALLLENGTH)
w4.rect.move_ip(0,HEIGHT-WALLLENGTH)
w4.surf.fill(MAGENTA)
downWalls.add(w4)

# create a box
b1 = Box("b1",CYAN,350,250,450,350)
b2 = Box("b2",YELLOW,450,250,550,350)
b3 = Box("b3",YELLOW,350,350,450,450)
b4 = Box("b4",CYAN,450,350,550,450)
b5 = Box("b5",CYAN,350,450,450,550)
b6 = Box("b6",YELLOW,450,450,550,550)
b7 = Box("b7",CYAN,550,450,650,550)


RUNNING = True

FIRSTTIME = True

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
            pygame.quit()
        elif (event.type == QUIT):
            RUNNING = False
            pygame.quit()
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            if DEBUG == True:
                print(p.rect)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    try:
        pressedKeys = pygame.key.get_pressed()
    
        # and then send that dictionary to the Person object for them to
        # update themselves accordingly.
        p.update(pressedKeys)

        # fill the screen with a color
        screen.fill(WHITE)
        # then transfer the person and walls to the screen
        if FIRSTTIME == True:
            screen.blit(p.surf, p.rect)
            p.rect.move_ip(WIDTH/2+100,HEIGHT/2-150)
            FIRSTTIME = False
        else:
            screen.blit(p.surf, p.rect)

        w1.wallBlit()
        w2.wallBlit()
        w3.wallBlit()
        w4.wallBlit()
        b1.boxBlit()
        b2.boxBlit()
        b3.boxBlit()
        b4.boxBlit()
        b5.boxBlit()
        b6.boxBlit()
        b7.boxBlit()
        
        pygame.display.flip()

        # detect collision with walls
        if pygame.sprite.spritecollideany(p,leftWalls):
            p.goRight()
        if pygame.sprite.spritecollideany(p,upWalls):
            p.goDown()
        if pygame.sprite.spritecollideany(p,rightWalls):
            p.goLeft()
        if pygame.sprite.spritecollideany(p,downWalls):
            p.goUp()
    except:
        pass
