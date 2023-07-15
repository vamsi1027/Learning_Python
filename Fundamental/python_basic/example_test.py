from abc import ABCMeta, abstractmethod


class DataFormat(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class TextFormat(DataFormat):
    def update(self):
        print("Test Data")


class Client:
    def __init__(self):
        self.data_format = []

    def attach(self, data_format: DataFormat):
        self.data_format.append(data_format)

    def get_data(self):
        for format_one in self.data_format:
            print(format_one.update())


if __name__ == "__main__":
    client = Client()
    text_array = [TextFormat(), TextFormat(), TextFormat()]

    for text in text_array:
        client.attach(text)

    client.get_data()
