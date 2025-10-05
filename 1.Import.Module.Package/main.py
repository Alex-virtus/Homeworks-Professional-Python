import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    dt = datetime.datetime.now()
    current_date = dt.date()
    print(f'Текущая дата: {current_date}')
    calculate_salary()
    get_employees()
