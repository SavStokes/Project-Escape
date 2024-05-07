##########################################################
# Noah Folse
#start: 3 April 2024
#Final Project Game Framework *Code Subject to change as program specifics become known
##########################################################
import pygame
from time import sleep
from Item import *
from Constants import *

DEBUG = False


#fix box swapping


#class of movable objects directly controlled by the player(DirConMoveable=Direct Control Movable)
class DirConMoveable(pygame.sprite.Sprite,Item):
    
    def __init__(self):
        super().__init__()
        super(pygame.sprite.Sprite,self).__init__()
        self.color = CYAN
        self.number = "3"
        surf=pygame.Surface((self.sizeX,self.sizeY))
        self.surf = surf
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        self.text = font.render(self.number,True,(0,0,0))
        self.x = WIDTH/2+100
        self.y = HEIGHT/2-150
        
    def update(self, pressedKeys):
        if pressedKeys[K_UP]:
            self.goUp()
            self.y -= 1
            sleep(UTIMER)
        elif pressedKeys[K_DOWN]:
            self.goDown()
            self.y += 1
            sleep(UTIMER)
        elif pressedKeys[K_LEFT]:
            self.goLeft()
            self.x -= 1
            sleep(UTIMER)

        elif pressedKeys[K_RIGHT]:
            self.goRight()
            self.x += 1
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

        #box Middle
        self.boxCenter = Immoveable(self.name+"Center",self.lengthX+4,self.lengthY+4)
        self.boxCenter.rect = self.boxCenter.surf.get_rect()
        self.boxCenter.rect.move_ip(self.topLeftX,self.topLeftY)
        self.boxCenter.surf.fill(self.color)

        #box Text
        self.boxText = font.render(self.name,True,(0,0,0))


    def boxBlit(self):
        screen.blit(self.boxLeft.surf,self.boxLeft.rect)
        screen.blit(self.boxTop.surf,self.boxTop.rect)
        screen.blit(self.boxRight.surf,self.boxRight.rect)
        screen.blit(self.boxDown.surf,self.boxDown.rect)
        screen.blit(self.boxCenter.surf, self.boxCenter.rect)
        screen.blit(self.boxText,self.boxCenter.rect)

    def moveBox(self,newX, newY):
        self.boxLeft.rect.move_ip(newX,newY)
        self.boxTop.rect.move_ip(newX,newY)
        self.boxRight.rect.move_ip(newX,newY)
        self.boxDown.rect.move_ip(newX,newY)
        self.boxCenter.rect.move_ip(newX,newY)
        self.topLeftX += newX
        self.bottomRightX += newX
        self.topLeftY += newY
        self.bottomRightY += newY


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
    
def findPosition(x, y):
    if 350 <= x < 450:
        if 250 <= y < 350:
            return (350,250)           
        if 350 <= y < 450:
            return (350,350)
        if 450 <= y < 550:
            return (350,450)
    if 450 <= x < 550:
        if 250 <= y < 350:
            return (450,250)
        if 350 <= y < 450:
            return (450,350)
        if 450 <= y < 550:
            return (450,450)
    if 550 <= x < 650:
        if 250 <= y < 350:
            return (550,250)
        if 350 <= y < 450:
            return (550,350)
        if 450 <= y < 550:
            return (550,450)

def switchPosition(leftX, rightX, topY, bottomY):
    playerSurf = p.surf
    playerText = p.text
    playerNum = p.number
    for box in boxes:
        if leftX <= (box.topLeftX + box.bottomRightX)/2 <= rightX and topY <= (box.topLeftY + box.bottomRightY)/2 <= bottomY:
            newX,newY = findPosition(p.x,p.y)
            box.moveBox(newX-box.topLeftX,newY-box.topLeftY)
            p.rect.move_ip(leftX-newX,topY-newY)
            p.x += leftX-newX
            p.y += topY-newY
            p.surf = box.boxCenter.surf
            box.boxCenter.surf = playerSurf
            p.text = box.boxText
            box.boxText = playerText
            p.number = box.name
            box.name = playerNum
            


def checkWin():
    correctBoxes = []
    for box in boxes:
        if box.name == "1":
            if box.topLeftX == 350 and box.topLeftY == 250:
                correctBoxes.append("1")
        elif box.name == "2":
            if box.topLeftX == 450 and box.topLeftY == 250:
                correctBoxes.append("2")
        elif box.name == "3":
            if box.topLeftX == 550 and box.topLeftY == 250:
                correctBoxes.append("3")
        elif box.name == "4":
            if box.topLeftX == 350 and box.topLeftY == 350:
                correctBoxes.append("4")
        elif box.name == "5":
            if box.topLeftX == 450 and box.topLeftY == 350:
                correctBoxes.append("5")
        elif box.name == "7":
            if box.topLeftX == 350 and box.topLeftY == 450:
                correctBoxes.append("7")
        elif box.name == "8":
            if box.topLeftX == 450 and box.topLeftY == 450:
                correctBoxes.append("8")
        elif findPosition(p.x,p.y) == (550,350):
            correctBoxes.append("6")
        if correctBoxes == ["7","8","2","3","1","4","5"]:
            win()
        else:
            pass


def win():
    print("You Win!")
    RUNNING = False

            
    

######################################
#MAIN: For testing purposes
######################################

# initialize pygame and display
pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(),100)
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
b1 = Box("2",CYAN,350,250,450,350)
b2 = Box("8",YELLOW,450,250,550,350)
b3 = Box("1",YELLOW,350,350,450,450)
b4 = Box("5",CYAN,450,350,550,450)
b5 = Box("4",CYAN,350,450,450,550)
b6 = Box("7",YELLOW,450,450,550,550)
b7 = Box("6",CYAN,550,450,650,550)

boxes = [b1,b2,b3,b4,b5,b6,b7]

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 350 <= mouse[0] <= 450:
                if 250 <= mouse[1] <= 350:
                    switchPosition(350,450,250,350)
                if 350 <= mouse[1] <= 450:
                    switchPosition(350,450,350,450)
                if 450 <= mouse[1] <= 550:
                    switchPosition(350,450,450,550)
            if 450 <= mouse[0] <= 550:
                if 250 <= mouse[1] <= 350:
                    switchPosition(450,550,250,350)
                if 350 <= mouse[1] <= 450:
                    switchPosition(450,550,350,450)
                if 450 <= mouse[1] <= 550:
                    switchPosition(450,550,450,550)
            if 550 <= mouse[0] <= 650:
                if 250 <= mouse[1] <= 350:
                    switchPosition(550,650,250,350)
                if 350 <= mouse[1] <= 450:
                    switchPosition(550,650,350,450)
                if 450 <= mouse[1] <= 550:
                    switchPosition(550,650,450,550)
            

    mouse = pygame.mouse.get_pos()
    
    checkWin()
    
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
            screen.blit(p.text, p.rect)
            

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
            p.x += 1

        if pygame.sprite.spritecollideany(p,upWalls):
            p.goDown()
            p.y += 1

        if pygame.sprite.spritecollideany(p,rightWalls):
            p.goLeft()
            p.x -= 1
        if pygame.sprite.spritecollideany(p,downWalls):
            p.goUp()
            p.y -= 1



    except:
        pass
