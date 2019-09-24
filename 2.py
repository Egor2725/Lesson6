import math
class Circle():
    def __init__(self, r):
        self.r=r

    def show_area(self):
        area = math.pi * float(self.r**2)
        print(area)

circle1 = Circle(10)
circle1.show_area()

input()
