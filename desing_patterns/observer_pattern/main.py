import pygame

from practices.desing_patterns.observer_pattern.circle import Circle
from practices.desing_patterns.observer_pattern.rectangle import Rectangle


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Observer Design Pattern with pygram")

    running = True
    clock = pygame.time.Clock()

    # Instance of our  Publisher
    circle = Circle(400, 300, 50, (255, 255, 255))

    # Three instance of our subscriber/observer classes
    rectangles = [
        Rectangle(100, 100, 50, 50, (255, 0, 0)),
        Rectangle(200, 200, 50, 50, (0, 255, 0)),
        Rectangle(300, 300, 50, 50, (0, 0, 255))
    ]

    for rect in rectangles:
        circle.attach(rect)

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        circle.draw(screen)

        for rect in rectangles:
            rect.draw(screen)

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            circle.move(*mouse_pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
