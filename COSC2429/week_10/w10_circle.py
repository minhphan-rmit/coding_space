from math import pi


class Circle:
    def __init__(self, radius):
        """Initialize radius attributes"""
        self.radius = radius

    def get_radius(self):
        """Get the radius of the circle"""
        return self.radius

    def change_radius(self, new_radius):
        """Change the radius of the circle"""
        self.radius = new_radius

    def get_area(self):
        """Calculate the area of the circle"""
        return (self.radius ** 2) * pi

    def get_perimeter(self):
        """Calculate the perimeter of the circle"""
        return (self.radius * 2) * pi


circy = Circle(int(input('Enter the radius of the circle: ')))
print(circy.get_area())
print(circy.get_perimeter())
print(circy.radius)
