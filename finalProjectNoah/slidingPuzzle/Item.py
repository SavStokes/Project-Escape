#####################################################################
# author:Noah Folse 
# date:22 March 2024    
# description: A class that stores name, location, and size data of a "person"
#####################################################################
from Constants import *
import pygame

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600


# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Item:
    def __init__(self, name="player 1", sizeX=100, sizeY=100):
        self.name = name
        self.sizeX = sizeX
        self.sizeY = sizeY

#name getter and setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, newName):
        if len(newName) > 1:
            self._name = newName
        else:
            self._name = "player 1"

#size getter and setter
    @property
    def sizeX(self):
        return self._sizeX
    @sizeX.setter
    def sizeX(self, newSize):
        if newSize >= 1:
            self._sizeX = newSize
        else:
            self._sizeX = self.sizeX
    @property
    def sizeY(self):
        return self._sizeY
    @sizeY.setter
    def sizeY(self, newSize):
        if newSize >= 1:
            self._sizeY = newSize
        else:
            self._sizeY = self.sizeY

#makes the person "go left" by decreasing x by 1
    def goLeft(self, distance=1):
        self.rect.move_ip(-distance,0)
        

#makes the person "go right" by increasing x by 1
    def goRight(self, distance=1):
        self.rect.move_ip(distance,0)

#makes the person "go up" by decreasing y by 1
    def goUp(self, distance=1):
        self.rect.move_ip(0,-distance)

#makes the person "go down" by increasing y by 1
    def goDown(self, distance=1):
        self.rect.move_ip(0,distance)

#returns the string of important information on specified instance
    def __str__(self):
        return f"{self.name}: \t sizeX={self.sizeX}, \t sizeY={self.sizeY}"
