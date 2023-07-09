from practices.desing_patterns.state_pattern.traffic_light_state import TrafficLightState
from practices.desing_patterns.state_pattern.colore import Color


class GreenState(TrafficLightState):

    def get_color(self) -> Color:
        return Color.GREEN

    def next(self, light: "traffic_light") -> None:
        light.current_state = GreenState()
