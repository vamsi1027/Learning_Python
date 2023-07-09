from practices.desing_patterns.state_pattern.traffic_light_state import TrafficLightState
from practices.desing_patterns.state_pattern.colore import Color


class YellowState(TrafficLightState):

    def get_color(self) -> Color:
        return Color.YELLOW

    def next(self, light: "traffic_light") -> None:
        light.current_state = YellowState()
