import csv
import pprint
from pprint import pprint

from phonebook.contacts import normalize_contacts


def main():
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    final_contacts = normalize_contacts(contacts_list)

    pprint(final_contacts)

    # Сохраняем результат в формат CSV
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(final_contacts)


if __name__ == "__main__":
    main()
