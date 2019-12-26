import Contact


def print_phone_book(caption, contacts):
    string = list()
    for contact in contacts:
        string.append(f"{contact.__str__()}")
    if len(contacts) > 0:
        return f"{caption}:\n----------------------------\n" + "\n".join(string)
    else:
        return "Список номеров пуст.\n"


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = list()

    def __str__(self):
        return print_phone_book("Телефонная книга", self.contacts)

    def add_contact(self, first_name, last_name, phone_number, favorite=False, **kwargs):
        contact = Contact.Contact(first_name, last_name, phone_number, favorite, **kwargs)
        self.contacts.append(contact)

    def find_by_phone_number(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                return contact

    def find_by_name(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact

    def find_favorites_contacts(self):
        favorites_contacts = list()
        for contact in self.contacts:
            if contact.favorite:
                favorites_contacts.append(contact)
        return favorites_contacts

    def remove_contact(self, phone_number):
        contact = self.find_by_phone_number(phone_number)
        self.contacts.remove(contact)
