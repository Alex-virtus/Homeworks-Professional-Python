# import faker
from faker import Faker

fake = Faker()


def get_employees():
    print(f'Функция get_employees выполнена из модуля: {__name__}.')

    employees = []
    for _ in range(5):
        name = fake.name()
        email = fake.email()
        employees.append((name, email))
    print('Сгенерированы фейковые сотрудники:')

    for name, email in employees:
        print(f'Name: {name}, email: {email}')
    return employees
