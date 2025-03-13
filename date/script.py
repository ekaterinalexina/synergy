from datetime import datetime, date
# Функция для определения дня недели
def get_weekday(day, month, year):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birth_date = datetime(year, month, day)
    return week_days[birth_date.weekday()]
# Функция для определения високосного года
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
# Функция для определения возраста пользователя
def get_age(day, month, year):
    today = date.today()
    birth_date = date(year, month, day)
    age = today.year - birth_date.year - ((today.month,
    today.day) < (birth_date.month, birth_date.day))
    return age
# Функция для вывода цифр звездочками
def print_number_stars(number):
    digits = [
    [" *** ", "*   *", "*   *", "*   *", " *** "], #0
    ["  *  ", "* *  ", "  *  ", "  *  ", "*****"], #1
    [" *** ", "*   *", "   * ", " *   ", "*****"], #2
    ["*****", "    *", "*****", "    *", "*****"], #3
    ["*   *", "*   *", "*****", "    *", "    *"], #4
    ["*****", "*    ", "**** ", "    *", "**** "], #5
    ["*****", "*    ", "*****", "*   *", "*****"], #6
    ["*****", "   * ", "  *  ", " *   ", "*    "], #7
    ["*****", "*   *", "*****", "*   *", "*****"], #8
    ["*****", "*   *", "*****", "    *", "*****"] #9
    ]
    for row in range(5):
        line = ''.join(digits[int(digit)][row] + ' ' for digit in number)
        print(line)
        # Запрос данных у пользователя
day = int(input("Enter the day of your birth (DD): "))
month = int(input("Enter the month of your birth (MM): "))
year = int(input("Enter the year of your birth (YYYY): "))
# Определение дня недели
weekday = get_weekday(day, month, year)
print(f"Day of the week: {weekday}")
# Определение високосного года
leap_year = is_leap_year(year)
print(f"Leap year: {'Yes' if leap_year else 'No'}")
# Определение возраста пользователя
age = get_age(day,month,year)
print(f"Your age: {age} years")
# Вывод даты рождения звездочками
print("\nYour birth date in stars:")
print_number_stars(f"{day:02}")
print_number_stars(f"{month:02}")
print_number_stars(f"{year}")