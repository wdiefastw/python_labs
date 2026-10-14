import math
import random
import statistics
from datetime import date

print("=== Завдання 1 ===")
try:
    radius = float(input("Введіть радіус круга: "))
    katet1 = float(input("Введіть перший катет: "))
    katet2 = float(input("Введіть другий катет: "))
    items = int(input("Введіть загальну кількість предметів (N): "))
    capacity = int(input("Введіть місткість однієї упаковки (K): "))

    circle_area = math.pi * (radius ** 2)
    hypotenuse = math.sqrt(katet1 ** 2 + katet2 ** 2)
    packages = math.ceil(items / capacity)

    print(f"Площа круга: {round(circle_area, 2)}")
    print(f"Гіпотенуза: {round(hypotenuse, 2)}")
    print(f"Потрібно упаковок: {packages}")
except ValueError:
    print("Помилка: будь ласка, вводьте коректні числові значення.")

print("\n=== Завдання 2 ===")
try:
    n = int(input("Введіть кількість оцінок (N): "))
    if n <= 0:
        print("Помилка: Значення N повинно бути додатним!")
    else:
        grades = [random.randint(1, 12) for _ in range(n)]
        
        print(f"Оцінки: {grades}")
        print(f"Min: {min(grades)}")
        print(f"Max: {max(grades)}")
        print(f"Середнє: {round(statistics.mean(grades), 2)}")
        print(f"Медіана: {statistics.median(grades)}")
        
        high_grades_count = sum(1 for g in grades if 10 <= g <= 12)
        print(f"Оцінок 10–12: {high_grades_count}")
except ValueError:
    print("Помилка: введіть ціле число.")

print("\n=== Завдання 3 ===")
try:
    print("Введіть дату події:")
    year = int(input("Рік: "))
    month = int(input("Місяць (1-12): "))
    day = int(input("День: "))
    
    event_date = date(year, month, day)
    today_date = date.today()
    
    if event_date > today_date:
        diff = event_date - today_date
        print(f"До події залишилося: {diff.days} днів")
    elif event_date < today_date:
        diff = today_date - event_date
        print(f"Подія вже минула: {diff.days} днів тому")
    else:
        print("Подія відбувається сьогодні!")
except ValueError:
    print("Помилка: введено некоректну дату або неправильний формат чисел.")
