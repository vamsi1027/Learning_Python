import abc
from practices.desing_patterns.builder_pattern.sandwich_order import SandwichOrder


class SandwichBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = SandwichOrder()

    @abc.abstractmethod
    def add_bread(self):
        pass

    @abc.abstractmethod
    def add_filling(self):
        pass

    def get_result(self):
        return self.sandwich
