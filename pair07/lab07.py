
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Завдання 1.

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0
char_count = 0
longest_line = ""
longest_number = 0

for number, line in enumerate(lines, start=1):
    clean_line = line.strip()
    word_count += len(clean_line.split())
    char_count += len(line)

    if len(clean_line) > len(longest_line):
        longest_line = clean_line
        longest_number = number

print("Кількість рядків:", line_count)
print("Кількість слів:", word_count)
print("Кількість символів:", char_count)

if lines:
    print("Найдовший рядок: №", longest_number,
          ", ", len(longest_line), " символів", sep="")
    print("Текст:", longest_line)


# Завдання 2.

fragment = input("\nВведіть фрагмент тексту: ").lower()
found = False

with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        if fragment in line.lower():
            print(f"{number}: {line.strip()}")
            found = True

if not found:
    print("Збігів не знайдено.")


# Завдання 3.

students = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(";")
        score = int(score)

        if score > 80:
            students.append([name, score])

students.sort(key=lambda student: student[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in students:
        print(f"{name};{score}", file=file)

print("\nФайл result.txt створено.")


# Завдання 4.

def read_grades(filename):
    grades = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, subject, grade = line.strip().split(";")
            grade = int(grade)

            if name not in grades:
                grades[name] = []

            grades[name].append(grade)

    return grades


def calculate_averages(grades):
    results = []

    for name, marks in grades.items():
        average = sum(marks) / len(marks)
        results.append([name, len(marks), average])

    results.sort(key=lambda student: student[2], reverse=True)
    return results


grades = read_grades("grades.csv")
results = calculate_averages(grades)

with open("report.txt", "w", encoding="utf-8") as file:
    for name, count, average in results:
        print(f"{name} — оцінок: {count} — середній: {average:.2f}",
              file=file)

    if results:
        best_average = results[0][2]
        best_students = [
            name for name, count, average in results
            if average == best_average
        ]

        if len(best_students) == 1:
            print(
                f"Найкращий результат: {best_students[0]} — "
                f"{best_average:.2f}",
                file=file
            )
        else:
            names = " та ".join(best_students)
            print(
                f"Найкращий результат: {names} — {best_average:.2f}",
                file=file
            )

print("Файл report.txt створено.")
