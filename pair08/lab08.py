# Завдання 1
try:
    a = float(input("A: "))
    b = float(input("B: "))
    operation = input("Операція: ")
    
    if operation == "+":
        print("Результат:", a + b)
    elif operation == "-":
        print("Результат:", a - b)
    elif operation == "*":
        print("Результат:", a * b)
    elif operation == "/":
        print("Результат:", a / b)
    else:
        print("Помилка: невідома операція.")
except ValueError:
    print("Помилка: нечислове введення.")
except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна.")


# Завдання 2
def input_grade():
    while True:
        try:
            grade = int(input("Оцінка: "))
            if grade < 1 or grade > 12:
                raise ValueError("оцінка повинна бути від 1 до 12.")
            return grade
        except ValueError as error:
            if "от 1 до 12" in str(error) or "від 1 до 12" in str(error):
                print(f"Помилка: {error}")
            else:
                print("Помилка: потрібно ввести ціле число.")

grade = input_grade()
print("Прийнято:", grade)


# Завдання 3
students = ["Коваленко", "Мельник", "Шевченко", "Бондар"]
subjects = {"Математика": 95, "Фізика": 82, "Програмування": 100}

try:
    choice = int(input("1 - учень, 2 - предмет: "))
    if choice == 1:
        index = int(input("Індекс: "))
        print("Учень:", students[index])
    elif choice == 2:
        subject = input("Назва предмета: ")
        print("Оцінка:", subjects[subject])
    else:
        print("Помилка: невідомий пункт меню.")
except ValueError:
    print("Помилка: введено не ціле число.")
except IndexError:
    print("Помилка: учня з таким індексом немає.")
except KeyError:
    print("Помилка: такого предмета немає.")

# Завдання 4 і додаткове завдання
valid_records = []
correct_count = 0
skipped_count = 0
errors_list = []

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    for idx, line in enumerate(lines, 1):
        original_line = line.strip()
        if not original_line:
            continue
            
        if ";" not in original_line:
            reason = "відсутній роздільник або неправильна кількість полів"
            print(f"Рядок {idx} пропущено: {reason}.")
            errors_list.append(f"{idx};{reason};{original_line}")
            skipped_count += 1
            continue
            
        parts = original_line.split(";")
        if len(parts) != 2:
            reason = "відсутній роздільник або неправильна кількість полів"
            print(f"Рядок {idx} пропущено: {reason}.")
            errors_list.append(f"{idx};{reason};{original_line}")
            skipped_count += 1
            continue
            
        name, grade_str = parts[0].strip(), parts[1].strip()
        

        try:
            try:
                grade_float = float(grade_str)
            except ValueError:
                raise ValueError("бал не є числом")

            if not grade_float.is_integer():
                raise ValueError("бал не є цілим числом")
            
            grade = int(grade_float)

            if grade < 0 or grade > 100:
                raise ValueError("бал поза діапазоном")
                
            valid_records.append((name, grade))
            correct_count += 1

        except ValueError as error:
            reason = str(error)
            print(f"Рядок {idx} пропущено: {reason}.")
            errors_list.append(f"{idx};{reason};{original_line}")
            skipped_count += 1

    valid_records.sort(key=lambda x: x[1], reverse=True)

    with open("report.txt", "w", encoding="utf-8") as file_out:
        for name, grade in valid_records:
            file_out.write(f"{name};{grade}\n")

    if errors_list:
        with open("errors.txt", "w", encoding="utf-8") as file_err:
            for error_line in errors_list:
                file_err.write(f"{error_line}\n")

    print(f"Правильних записів: {correct_count}")
    print(f"Пропущено: {skipped_count}")
    print("Створено report.txt та errors.txt")

except FileNotFoundError:
    print("Помилка: файл students.txt відсутній.")


