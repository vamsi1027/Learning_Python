class EagerLoadingPattern(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(EagerLoadingPattern, new_class).__call__()
        return new_class

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]


class Singleton(metaclass=EagerLoadingPattern):
    def __init__(self):
        pass


singleton = Singleton()
print(singleton.__hash__())

singleton = Singleton()
print(singleton.__hash__())
