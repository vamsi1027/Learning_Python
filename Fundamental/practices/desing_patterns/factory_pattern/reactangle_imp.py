import random

import pygame.draw

from practices.desing_patterns.factory_pattern.shape_abstract_class import ShapeAbstract


class ReactAngleImp(ShapeAbstract):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.color = (random.randint(0, 225), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
