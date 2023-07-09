import abc


class FileReader(metaclass=abc.ABCMeta):
    def __init__(self, file_name):
        self.file_name = file_name

    @abc.abstractmethod
    def read(self, file_name) -> str:
        pass
