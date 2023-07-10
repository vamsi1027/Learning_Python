from abc import ABCMeta, abstractmethod


class WidgetRenderer(metaclass=ABCMeta):
    @abstractmethod
    def render(self, screen: str, ui_manager: str):
        pass
