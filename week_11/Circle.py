import math

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def obim(self):
        obim = 2 * self.get_radius() * math.pi()

    def povrsina(self):
        povrsina  = self.get_radius() ** 2 * math.pi


obj = Circle(15)

