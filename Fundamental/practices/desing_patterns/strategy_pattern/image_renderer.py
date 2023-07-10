from practices.desing_patterns.strategy_pattern.widget_render import WidgetRenderer
import pygame


class ImageRenderer(WidgetRenderer):
    def __init__(self, image_path, size):
        self.image_path = image_path
        self.image = None
        self.size = size

    def load_image(self):
        str = self.image_path
        self.image = pygame.image.load(self.image_path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def render(self, screen: str, ui_manager: str):
        if not self.image:
            self.load_image()
        screen.blit(self.image, (200, 70))
        return "Rendering an image...", None
