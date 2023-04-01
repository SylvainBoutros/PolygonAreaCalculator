class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.__class__.__name__ == "Rectangle":
            return f'Rectangle(width={self.width}, height={self.height})'
        else:
            return f'Square(side={self.width})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        results = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                results += "*" * self.width
                results += "\n"

            return results
        else:
            return "Too big for picture."

    def get_amount_inside(self, obj):
        if isinstance(obj, Square):
            return self.get_area() // obj.get_area()
        elif isinstance(obj, Rectangle):
            return self.get_area() // obj.get_area()
        else:
            raise TypeError('get_amount_inside() accepts only Square or Rectangle as argument')


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, width):
        self.width = width
        self.height = width

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def get_area(self):
        return self.width ** 2


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
