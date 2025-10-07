def merge_contacts(contacts):
    # Объединяем дубли, дополняя пустые значения
    header = contacts[0]
    merged = {}

    for contact in contacts[1:]:
        key = (contact[0], contact[1])
        if key not in merged:
            merged[key] = contact
        else:
            for i in range(len(contact)):
                if merged[key][i] == "":
                    merged[key][i] = contact[i]
    return [header] + list(merged.values())
