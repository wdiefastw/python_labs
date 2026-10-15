import os
from pydoc import text

if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування.\n")
        file.write("Python використовується для роботи з даними.\n")
        file.write("Файли дозволяють зберігати інформацію\n")
        file.write("Python вимагає практики.\n")
        file.write("Сьогодні ми працюємо з текстовими файлами.\n")

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76\n")
        file.write("Komarova Sophie;97\n")
        file.write("Bondarenko Illya;84\n")

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6\n")
        file.write("Ivan;Math;5\n")
        file.write("Sophie;Python;11\n")
        file.write("Sophie;Math;12\n")
        file.write("Illya;Python;9\n")
        file.write("Illya;Math;8\n")

# with open('hello.txt', 'w', encoding="utf-8") as file:
#     file.write("Hello world2!!!!\n")
#     file.write("Hello world3!!!!\n")
#     file.write("Hello world4!!!!\n")


#w - режим запису (створює файл або перезаписує існуючий)
# r - режим читання (файл повинен існувати)
# a - режим додавання (додає дані в кінець файлу)
# b - бінарний режим (для роботи з бінарними файлами)
# x - режим створення (створює файл, якщо він не існує, і викликає помилку, якщо файл вже існує)

# with open("text.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# print(f'read() => \n{text} \nlen() => {len(text)}')


# with open("text.txt", "r", encoding="utf-8") as file:
#     line1 = file.readline()
#     other_lines = file.readlines()
#     line2 = file.readline()
    

# print(line1)
# print(other_lines)
# print(line2)


# with open("text.txt", "r", encoding="utf-8") as file:
#     other_lines = file.readlines()
# for line in other_lines:
#     print(line)


# with open("text.txt", "r", encoding="utf-8") as file:
#     for number, line in enumerate(file, start=1):
#         clean_line = line.strip()
#         print(f'{number}. {clean_line}')

# line = "Komarov Ivan;2\n"
# clean_line = line.strip()
# name, grade = clean_line.split(";")
# print(name)
# print(grade)


# students = []
# botanics = []
# with open('students.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         name, grade = line.strip().split(';')
#         students.append([name, grade])
#         if int(grade) >= 90:
#             botanics.append([name, grade])
# print(students)
# print(botanics)

# with open('botanics.txt', 'w', encoding="utf-8") as file:
#     for name, grade in botanics:
#         file.write(name + ';' + grade + '\n')

grades = []
with open("grades.csv", "r", encoding="utf-8") as file:
    for line in file:
        name, subject, grade = line.strip().split(";")
        grades.append(grade)
        print(f"Ім'я: {name}. Предмет: {subject}. Оцінка: {grade}")
average = sum(int(g) for g in grades) / len(grades)
print(f"Середня оцінка: {average}")
