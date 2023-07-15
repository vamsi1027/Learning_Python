import json

from practices.desing_patterns.adapter_pattern.adapters.contact_adapter import ContactAdapter
from practices.desing_patterns.adapter_pattern.dataclass.contact import Contact


class JsonAdapterReader(ContactAdapter):
    def get_contact(self) -> list[Contact]:
        data_dict = json.loads(self.data_source.read())
        contacts = []
        for contact_data in data_dict['contact']:
            full_name = contact_data['full_name']
            email = contact_data['email']
            phone_number = contact_data['phone_number']
            is_friend = contact_data['is_friend']
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        return contacts
