class Shape:
   
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length=length

    def area(self):
        return self.length ** 2


square = Square(length=4)

print(f"Area of the square: {square.area()}")
