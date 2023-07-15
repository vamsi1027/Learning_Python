import pygame
import random

from practices.desing_patterns.observer_pattern.observer_abc import ObserverABC


class Rectangle(ObserverABC):

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        #print("subject :", subject)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
