import abc
from abc import ABCMeta
from practices.desing_patterns.state_pattern.colore import Color


class TrafficLightState(metaclass=ABCMeta):

    @abc.abstractmethod
    def next(self, light: "TrafficLight") -> None:
        pass

    @abc.abstractmethod
    def get_color(self) -> Color:
        pass
