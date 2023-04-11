class Shape: #parent 
    shape_type = 'shape'

    def calculate_area(self):
        pass
        def print_result(self):
        print('The area of', shape_type, 'is', self.caluate.area())
        

#nana
#a new class from an existinf class
#polysomething
class Circle(Shape): #child class
    shape_type = 'Circle'

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    shape_type ='Square'
    def __init__(self, length, witdth):
        self.length = length
        self.width = witdth

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height 
    
    def calculate_area(self):
        return 0.5* self.base * self.height
    
little_circle = Circle(10)
little_square = Square(5, 4)
little_triangle = Triangle(4, 5)

little_circle.calculate_area()
little_square.calculate_area()
little_triangle.calculate_area()

print('The areas of a circle is', little_circle.calculate_area())
print('Thea area of a square is', little_square.calculate_area())
print('The area of a triangle', little_triangle.calculate_area())