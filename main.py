from datetime import date

from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_date = date.today()
    print(current_date)
