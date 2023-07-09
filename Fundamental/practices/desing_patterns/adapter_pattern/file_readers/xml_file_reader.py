from practices.desing_patterns.adapter_pattern.file_readers.file_reader import FileReader


class XMLFileReader(FileReader):
    def read(self) -> str:
        with open(self.file_name, 'r') as f:
            return f.read()
