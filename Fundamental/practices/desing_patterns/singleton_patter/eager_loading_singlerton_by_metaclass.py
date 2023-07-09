class EagerLoadingSingleton(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]


class Singleton(metaclass=EagerLoadingSingleton):
    def __init__(self):
        pass


singleton = Singleton()
print(singleton.__hash__())

singleton = Singleton()
print(singleton.__hash__())
