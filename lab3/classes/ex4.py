import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        return  f"x is {self.x} and y is {self.y}"
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
        return f"x has moved to {self.x} and y has moved to {self.y}"
    def dist(self,dx,dy):
        dist=((dx-self.x)**2+(dy-self.y)**2)**0.5
        return dist
points=Point(x=2,y=5)
print(points.show())
print(points.move(4,3))
print(f"the distance is {points.dist(2,7)}")


