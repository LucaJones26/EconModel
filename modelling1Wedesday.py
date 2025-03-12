#point
import random

class Point:
    def __init__(self, x, y): #we are linkin the points of x and y, turning numbers into coordinates
        """ #self can be anything else as long as they are same in the parenthesis, self most commonly used though
        Initializa a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x #define x attribute via self.x
        self.y = y #and assign the value x to it

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x, y>
        """
        return f"<{self.x}, {self.y}>"
    def distance_orig(self):
        return(self.x**2 + self.y**2)**0.5 #square root of the sum of x and y (pythagorean theorem)

#now we need to instantiate

p = Point(1,2) #p is an instance of 1 and 2
p2 = Point(2, 3)
p4 = Point(4.4, -55)
print(p.x, p.y) #prints x and y value above
print(f"p4.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
#can change this information too
p.x = 20
print(f"p4.x={p.x} and p.y={p.y}")
print(p) #


#create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10,10 ), # x value
                        random.randint(-10, 10))) # y value
print("I got these 5 random points:")
for p in points:
    print(p)


    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__ (self):
        return self.__str__() #use the same way as printing as str



# this session learnt to establish points and randomise numbers

#