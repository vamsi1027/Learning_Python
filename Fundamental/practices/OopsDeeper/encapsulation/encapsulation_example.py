class MyEncapsulation:
    __name: str
    __id: int
    __location: str

    def __init__(self, name=None, id=None, location=None):
        self.__name = name  # private property
        self.__id = id  # private property
        self.__location = location  # private property

    def get_name(self):
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_location(self, location: str) -> None:
        self.__location = location

    def get_location(self):
        return self.__location

    def set_id(self, id: int) -> None:
        self.__id = id


my_obj = MyEncapsulation('vamsi', 'Hyd', 123)

print(my_obj.set_location("USA"))
print(my_obj.get_location())
