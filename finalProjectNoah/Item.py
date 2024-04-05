#####################################################################
# author:Noah Folse 
# date:22 March 2024    
# description: A class that stores name, location, and size data of a "person"
#####################################################################
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
    def __init__(self, name="player 1", x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 1

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

#x getter and setter
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, newX):
        if newX < 0:
            self._x = 0
        elif newX > MAX_X:
            self._x = MAX_X
        else:
            self._x = newX

#y getter and setter
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, newY):
        if newY < 0:
            self._y = 0
        elif newY > MAX_Y:
            self._y = MAX_Y
        else:
            self._y = newY

#size getter and setter
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, newSize):
        if newSize >= 1:
            self._size = newSize
        else:
            self._size = self.size

#makes the person "go left" by decreasing x by 1
    def goLeft(self, distance=1):
        self.x -= distance

#makes the person "go right" by increasing x by 1
    def goRight(self, distance=1):
        self.x += distance

#makes the person "go up" by decreasing y by 1
    def goUp(self, distance=1):
        self.y -= distance

#makes the person "go down" by increasing y by 1
    def goDown(self, distance=1):
        self.y += distance

#calculates the distance by using the euclidian distance formula
#((x2-x1)^2+(y2-y1)^2)^(1/2)
    def getDistance(self, other):
        return ((self.x - other.x)**2+(self.y - other.y)**2)**(1/2)
    
#returns the string of important information on specified instance
    def __str__(self):
        return f"{self.name}: \t size={self.size}, \t x={self.x} \t y={self.y}"
