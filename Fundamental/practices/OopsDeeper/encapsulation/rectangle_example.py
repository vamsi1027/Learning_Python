class Rectangle:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value:int):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value


my_react = Rectangle(10, 20)
print(my_react.__getattribute__('width'))
print(my_react.width)
