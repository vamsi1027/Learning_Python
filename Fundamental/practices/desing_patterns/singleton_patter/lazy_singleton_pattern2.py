class BasicSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


singleton = BasicSingleton()
print(singleton.__hash__())
singleton = BasicSingleton()
print(singleton.__hash__())
