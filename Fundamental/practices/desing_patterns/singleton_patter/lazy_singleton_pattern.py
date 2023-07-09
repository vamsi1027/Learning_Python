class ClassicSingle:
    # TODO: class-level variable to store single class instance
    _instance = None

    # TODO override the _init_ method to constrole initialize
    def __init__(self):
        # TODO: Raise an error to prevent constructor initialization
        raise RuntimeError("Call Instance() method")

    @classmethod
    def get_instance(cls):
        if not cls._instance:  # TODO: NOTE lazy initialization
            # TODO: create new instance of the class
            cls._instance = cls.__new__(cls)
            # TODO: Return the singleton instance of the class, either
            # TODO: newly created one or existing one
        return cls._instance


singleton = ClassicSingle.get_instance()
print(singleton.__hash__())
singleton = ClassicSingle.get_instance()
print(singleton.__hash__())
