import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return'<'+'Shape x='+str(self.x)+' y='+str(self.y)+'>'

    def area(self):
        print(self.x * self.y)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return '<' + 'Circle x=' + str(self.x) + ' y=' + str(self.y) + ' Radius='+str(self.radius) + '>'

    def area(self):
        print(math.pi * self.radius ** 2)

    def circumference(self):
        print(2 * math.pi * self.radius)


class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return '<' + 'Rectangle x=' + str(self.x) + ' y=' + str(self.y) + '>'

    def area(self):
        print(self.x * self.y)


class Square(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return'<' + 'Square x=' + str(self.x) + ' y=' + str(self.y) + '>'

    def area(self):
        print(self.x * self.y)


class Triangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return '<' + 'Triangle x=' + str(self.x) + ' y=' + str(self.y) + '>'

    def area(self):
        print(self.x * self.y * 0.5)

p = Shape(1, 1)
print(p)
p.area()

a = Circle(3, 4, 7)
print(a)
a.area()
a.circumference()

b = Rectangle(2, 8)
print(b)
b.area()

c = Square(4, 4)
print(c)
c.area()

d = Triangle(4, 6)
print(d)
d.area()