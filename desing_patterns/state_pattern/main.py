import random
import time

from practices.desing_patterns.state_pattern.colore import Color
from practices.desing_patterns.state_pattern.traffic_light import TrafficLight
from practices.desing_patterns.state_pattern.green_state import GreenState
from practices.desing_patterns.state_pattern.yellow_state import YellowState
from practices.desing_patterns.state_pattern.red_state import RedState

import pygame


class TrafficLightSimulation:

    def __init__(self):
        self.light = TrafficLight()
        self.cycle = 0
        self.screen = None
        self.width = 400
        self.height = 800

    def start(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Traffic Light Simulation")

        traffic_single = [GreenState(), RedState(), YellowState()]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.light.traffic_single(traffic_single[random.randint(0, 2)])
            self.cycle += 1
            self.light.next()

            self.draw()
            pygame.display.update()
            time.sleep(2)

    def stop(self) -> None:
        pygame.quit()

    def draw(self) -> None:
        self.screen.fill((211, 211, 211))

        red_color = (255, 0, 0)
        yellow_color = (255, 255, 0)
        green_color = (0, 255, 0)

        outline_color = (70, 70, 70)

        rect_x = self.width // 4
        rect_y = self.height // 8
        rect_width = self.width // 2
        rect_height = self.height // 1.5

        pygame.draw.rect(self.screen, outline_color, (rect_x, rect_y, rect_width, rect_height), 10)

        radius = 50
        center_x = self.width // 2
        center_y = self.height // 2

        pygame.draw.circle(self.screen, outline_color, (center_x, center_y - (rect_height // 4)), radius + 5, 5)
        if self.light.get_color() == Color.RED:
            pygame.draw.circle(self.screen, red_color, (center_x, center_y - (rect_height // 4)), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y - (rect_height // 4)), radius)

        pygame.draw.circle(self.screen, outline_color, (center_x, center_y), radius + 5, 5)
        if self.light.get_color() == Color.YELLOW:
            pygame.draw.circle(self.screen, yellow_color, (center_x, center_y), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y), radius)

        pygame.draw.circle(self.screen, outline_color, (center_x, center_y + (rect_height // 4)), radius + 5, 5)
        if self.light.get_color() == Color.GREEN:
            pygame.draw.circle(self.screen, green_color, (center_x, center_y + (rect_height // 4)), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y + (rect_height // 4)), radius)


if __name__ == "__main__":
    simulation = TrafficLightSimulation()

    try:
        #simulation.start()
      print(__name__)
    except KeyboardInterrupt:
        simulation.stop()
