import math

def area_circle(radius):
    return 3.14159 * radius * radius

def area_rectangle(a, b):
    return a * b

def area_triangle(a, h):
    return 0.5 * a * h

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def average(numbers):
    return sum(numbers) / len(numbers)

def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

def input_grades():
    string_grades = input("Введіть оцінки через пробіл: ")
    print("Поріг:9")
    return [int(x) for x in string_grades.split()]

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("немає мінімальної довжини")
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    if not has_digit:
        errors.append("немає хоча б однієї цифри")
        
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
    if not has_upper:
        errors.append("великої літери")
        
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
    if not has_lower:
        errors.append("малої літери")
        
    has_special = False
    for char in password:
        if not char.isalnum():
            has_special = True
    if not has_special:
        errors.append("немає спеціального символу")
        
    return len(errors) == 0, errors

def print_report(grades):
    print("Середній бал:", round(average(grades), 2))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print("Вище 9:", count_above(grades, 9))

def main():
    print("=== Завдання 1 ===")
    shape = input("Фігура: ")
    if shape == "прямокутник":
        width = float(input("Ширина: "))
        height = float(input("Висота: "))
        result = area_rectangle(width, height)
        print("Площа прямокутника:", result)
    elif shape == "круг":
        radius = float(input("Радіус: "))
        result = area_circle(radius)
        print("Площа круга:", result)
    elif shape == "трикутник":
        base = float(input("Основа: "))
        h = float(input("Висота: "))
        result = area_triangle(base, h)
        print("Площа трикутника:", result)

    print("\n=== Завдання 2 ===")
    grade = int(input("N = "))
    if is_prime(grade):
        print("Просте число: так")
    else:
        print("Просте число: ні")
    print("Дільники:", divisors(grade))
    print("Сума цифр:", digit_sum(grade))

    print("\n=== Завдання 3 ===")
    grades = input_grades()
    print_report(grades)

    print("\n=== Завдання 4 ===")
    password = input("Password: ")
    is_valid, failed_requirements = validate_password(password)
    if is_valid:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        for error in failed_requirements:
            print("Не виконано:", error)

main()
