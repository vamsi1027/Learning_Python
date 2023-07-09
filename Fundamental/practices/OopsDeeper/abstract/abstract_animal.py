import abc


class Animal(abc.ABC):
    @abc.update_abstractmethods
    def make_sound(self):
        pass
