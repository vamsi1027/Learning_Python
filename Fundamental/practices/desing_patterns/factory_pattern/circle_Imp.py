import pygame as pygame

from practices.desing_patterns.factory_pattern.shape_abstract_class import ShapeAbstract
import random


class CircleImp(ShapeAbstract):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surface):
        pygame.draw.circle(surface,  self.color, (self.x, self.y), self.radius)
