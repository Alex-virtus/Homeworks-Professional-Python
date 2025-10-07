def normalize_fio(contact):
    # Приводим к виду Фамилия, Имя, Отчество
    fio = " ".join(contact[:3]).split()
    while len(fio) < 3:
        fio.append("")
    lastname, firstname, surname = fio[:3]
    return [lastname, firstname, surname] + contact[3:]
