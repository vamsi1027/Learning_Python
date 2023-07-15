import xml.etree.ElementTree as ET

from practices.desing_patterns.adapter_pattern.adapters.contact_adapter import ContactAdapter
from practices.desing_patterns.adapter_pattern.dataclass.contact import Contact


class XMLReaderAdapter(ContactAdapter):
    def get_contact(self) -> list[Contact]:
        root = ET.fromstring(self.data_source.read())
        contacts = []

        for elem in root.iter():
            if elem.tag == 'Contact':
                full_name = elem.find('full_name').text
                email = elem.find('email').text
                phone_number = elem.find('phone_number').text
                is_friend = elem.find('is_friend').text.lower() == True
                contact = Contact(full_name, email, phone_number, is_friend)
                contacts.append(contact)
        return contacts

