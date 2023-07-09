import random
import pygame

from practices.desing_patterns.factory_pattern import shape_factory
from practices.desing_patterns.factory_pattern.shape_factory import ShapeFactory
from practices.desing_patterns.factory_pattern.shape_context import ShapeContext
from practices.desing_patterns.factory_pattern.shape_type import ShapeType


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Yakshitha NotePad")
    clock = pygame.time.Clock()

    #shape_factory = ShapeFactory()
    shapes = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                shape_type = random.choice(list((ShapeType)))
                shape_context = ShapeContext(shape_type, x, y)
                shape = ShapeFactory.create_shape(shape_context)
                shapes.append(shape)
        screen.fill((255, 255, 255))

        for shape in shapes:
            shape.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
