from practices.desing_patterns.adapter_pattern.file_readers.file_reader import FileReader
from practices.desing_patterns.adapter_pattern.dataclass.contact import Contact
import abc


class ContactAdapter(metaclass=abc.ABCMeta):

    def __init__(self, data_source: FileReader):
        self.data_source = data_source

    @abc.abstractmethod
    def get_contact(self) -> list[Contact]:
        pass

