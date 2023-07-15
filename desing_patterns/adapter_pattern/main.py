from practices.desing_patterns.adapter_pattern.adapters.contact_adapter import ContactAdapter
from practices.desing_patterns.adapter_pattern.file_readers.xml_file_reader import XMLFileReader
from practices.desing_patterns.adapter_pattern.adapters.xml_reader_adapter import XMLReaderAdapter
from practices.desing_patterns.adapter_pattern.file_readers.json_file_reader import JsonFileReader
from practices.desing_patterns.adapter_pattern.adapters.json_reader_adapter import JsonAdapterReader


def main():
    def print_contact_data(contact_source: ContactAdapter):
        for contact in contact_source.get_contact():
            print(contact)

    xml_reader = XMLFileReader(
        "C://Users//Vamsi//PycharmProjects//Example//com//desing_patterns//adapter_pattern//test_data//User.xml")
    xml_adapter = XMLReaderAdapter(xml_reader)
    print_contact_data(xml_adapter)

    json_reader = JsonFileReader(
        "C://Users//Vamsi//PycharmProjects//Example//com//desing_patterns//adapter_pattern//test_data//User.json")
    json_adapter = JsonAdapterReader(json_reader)
    print_contact_data(json_adapter)


if __name__ == '__main__':
    main()
