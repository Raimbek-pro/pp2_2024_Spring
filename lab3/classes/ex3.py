class Shape:
   
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width


rec = Rectangle(length=4,width=6)

print(f"Area of the rectangle: {rec.area()}")
