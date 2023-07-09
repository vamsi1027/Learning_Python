class SingletonMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingleMain(metaclass=SingletonMetaClass):
    def some_bussiness_logic(self):
        pass


singletons = SingleMain()
print(singletons.__hash__())

singletons = SingleMain()
print(singletons.__hash__())
