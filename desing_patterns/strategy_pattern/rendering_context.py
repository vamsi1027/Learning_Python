from practices.desing_patterns.strategy_pattern.widget_render import WidgetRenderer


class RenderingContext:
    def __init__(self, renderer: WidgetRenderer):
        self._renderer = renderer

    def set_renderer(self, renderer: WidgetRenderer):
        self._renderer = renderer

    def render(self, screen, ui_manager):
        return self._renderer.render(screen, ui_manager)
