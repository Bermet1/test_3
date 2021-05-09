# Миксин

class Parent:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class PerimetrOfTriangle:
    def change(self, x):
        self.x += x
        self.y += x
        self.z += x

    def perimetr(self):
        return self.x + self.y + self.z

class ParentPerim(Parent, PerimetrOfTriangle):
    pass

triangle = ParentPerim(3, 4, 5)
triangle.perimetr()
print(triangle.perimetr())

triangle.change(10)
print(triangle.x)
print(triangle.perimetr())


