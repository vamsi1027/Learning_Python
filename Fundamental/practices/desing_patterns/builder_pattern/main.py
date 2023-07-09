import sys

import pygame
from practices.desing_patterns.builder_pattern.viggie_sandwich_builder import VeggieSandwichBuilder
from practices.desing_patterns.builder_pattern.sandwich_director import SandwichDirectory
from practices.desing_patterns.builder_pattern.ham_sandwich_builder import HamSandwichBuilder


def draw_text(screen, text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    # TODO: Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Sandwich Builder")
    font = pygame.font.Font(pygame.font.get_default_font(), 18)

    # TODO: Client code
    veggie_build = VeggieSandwichBuilder()
    director = SandwichDirectory(veggie_build)
    veggie_sandwich = director.build_sandwich()

    ham_build = HamSandwichBuilder()
    director = SandwichDirectory(ham_build)
    ham_sandwich = director.build_sandwich()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        draw_text(screen, "Veggie Sandwich", 10, 10, font, (0, 0, 0))
        for index, ingredient in enumerate(veggie_sandwich.ingredient):
            draw_text(screen, f"-{ingredient}", 10, 40 + index * 30, font, (2, 1, 1))

        draw_text(screen, "Ham Sandwich", 300, 10, font, (0, 0, 0))
        for index, ingredient in enumerate(ham_sandwich.ingredient):
            draw_text(screen, f"-{ingredient}", 300, 40 + index * 30, font, (0, 0, 0))

        pygame.display.flip()
        pygame.time.delay(100)
    pygame.quit()


if __name__ == "__main__":
    main()
