import pygame.time

from practices.desing_patterns.strategy_pattern.widget_render import WidgetRenderer
from moviepy.editor import *


class VideoRenderer(WidgetRenderer):
    def __init__(self, vide_path: str, size: any = None):
        self.vide_path = vide_path
        self.clip = None
        self.playing = False
        self.start_time = 0
        self.size = size

    def load_move(self):
        self.clip = VideoFileClip(self.vide_path)
        if self.size:
            self.clip = self.clip.resize(self.size)

    def render(self, screen: str, ui_manager: str):
        if not self.clip:
            self.load_move()
        current_time = pygame.time.get_ticks()
        if not self.playing:
            self.playing = True
            self.start_time = current_time
        if self.playing:
            elapsed_time = current_time - self.start_time
            if elapsed_time < self.clip.duration:
                frame = self.clip.get_frame(elapsed_time)
                frame = pygame.surface.make_subsurface(frame.swapaxes(0, 1))
                screen.blit(frame, (200, 70))
            else:
                self.playing = False
        return "Rendering a video", None

    def stop(self):
        self.playing = False





