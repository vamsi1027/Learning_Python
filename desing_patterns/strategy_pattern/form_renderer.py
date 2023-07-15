import pygame

from practices.desing_patterns.strategy_pattern.widget_render import WidgetRenderer
import pygame_gui


class FormRenderer(WidgetRenderer):
    def __init__(self):
        self.form_elements = None
        self.form_element = []
        self.panel = None

    def create_form(self, ui_manager):
        self.panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((300, 60), (260, 480)),
                                                 starting_layer_height=1,
                                                 manager=ui_manager,
                                                 object_id="form_panel",
                                                 anchors={"left", "left", "right", "right", "top", "top", "bottom",
                                                          "bottom"})
        self.form_element.append(pygame_gui.elements.UILable(relative_rect=pygame.Rect((300, 60), (260, 480)),
                                                             text="First Name",
                                                             manager=ui_manager, container=self.panel))
        self.form_element.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 60), (260, 480)),
                                                                     manager=ui_manager, container=self.panel))
        self.form_element.append(pygame_gui.elements.UILable(relative_rect=pygame.Rect((300, 60), (260, 480)),
                                                             text="Last Name",
                                                             manager=ui_manager, container=self.panel))
        self.form_element.append(pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 60), (260, 480)),
                                                                     manager=ui_manager, container=self.panel))
        self.form_element.append(
            pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 60), (260, 100)), text="Submit",
                                         manager=ui_manager, container=self.panel))

    def render(self, screen: str, ui_manager: str):
        if not self.form_elements:
            self.create_form_element(ui_manager)
        return "Rendering a form", None

    def clear_form(self):
        for element in self.form_elements:
            element.kill()
        self.form_elements = []
        if self.panel:
            self.panel.kill()
            self.panel = None
