import pygame
import pygame_gui

from practices.desing_patterns.strategy_pattern.form_renderer import FormRenderer
from practices.desing_patterns.strategy_pattern.image_renderer import ImageRenderer
from practices.desing_patterns.strategy_pattern.rendering_context import RenderingContext
from practices.desing_patterns.strategy_pattern.video_renderer import VideoRenderer


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Renderer Strategy Pattern Example")
    ui_manager = pygame_gui.UIManager((800, 600))

    context = RenderingContext(ImageRenderer(
        "C://Users//Vamsi//PycharmProjects//Example//com//desing_patterns//strategy_pattern//test_data//python_design_patterns.png",
        size=(550, 325)))

    image_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (100, 20)), text="Image",
                                                manager=ui_manager)

    video_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (100, 20)), text="Video",
                                                manager=ui_manager)

    widget_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (100, 20)), text="Widget",
                                                 manager=ui_manager)

    rendered_widget = None

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delata = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isinstance(context._renderer, FormRenderer):
                        context._renderer.clear_form()
                    if event.ui_element == image_button:
                        context.set_renderer(ImageRenderer(
                            "C://Users//Vamsi//PycharmProjects//Example//com//desing_patterns//strategy_pattern//test_data//python_design_patterns.png",
                            size=(550, 325)))
                    elif event.ui_element == video_button:
                        context.set_renderer(VideoRenderer(
                            "C://Users//Vamsi//PycharmProjects//Example//com//desing_patterns//strategy_pattern//test_data//example_video.mp4",
                            size=(550, 325)))
                    elif event.ui_element == widget_button:
                        context.set_renderer(FormRenderer())

            ui_manager.process_events(event)

        screen.fill((200, 200, 200))
        ui_manager.update(time_delata)
        ui_manager.draw_ui(screen)

        result_text, widget = context.render(screen, ui_manager)
        font = pygame.font.Font(None, 36)
        text = font.render(result_text, 1, (10, 10, 10))
        screen.blit(text, (300, 20))

        # Update the rendered widget.
        if rendered_widget:
            rendered_widget.kill()
        if widget:
            rendered_widget = widget

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
