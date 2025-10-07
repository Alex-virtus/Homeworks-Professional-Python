from .fio import normalize_fio
from .merge import merge_contacts
from .phone import normalize_phone


def normalize_contacts(contacts_list):
    # Нормализуем список контактов
    new_contacts = []
    for contact in contacts_list:
        if contact[0] == "lastname":
            new_contacts.append(contact)
            continue

        fixed = normalize_fio(contact)

        if fixed[5]:
            fixed[5] = normalize_phone(fixed[5])

        new_contacts.append(fixed)

    return merge_contacts(new_contacts)
