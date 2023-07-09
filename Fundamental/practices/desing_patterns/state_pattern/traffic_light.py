from practices.desing_patterns.state_pattern.red_state import RedState
from practices.desing_patterns.state_pattern.traffic_light_state import TrafficLightState
from practices.desing_patterns.state_pattern.green_state import GreenState
from practices.desing_patterns.state_pattern.colore import Color


class TrafficLight:
    current_state: TrafficLightState = GreenState()

    def next(self) -> None:
        self.current_state.next(self)

    def traffic_single(self, current_state):
        self.current_state = current_state
        self.next()

    def get_color(self) -> Color:
        return self.current_state.get_color()
