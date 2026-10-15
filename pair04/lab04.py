numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]

positive = []
negative = []
even = []
multiples_of_3 = []

for number in numbers:
    if number > 0:
        positive.append(number)
    if number < 0:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    if number % 3 == 0:
        multiples_of_3.append(number)

min_val = min(numbers)
max_val = max(numbers)
sum_val = sum(numbers)
average_val = sum_val / len(numbers)

print("--- Завдання 1 ---")
print("Додатні:", positive)
print("Від’ємні:", negative)
print("Парні:", even)
print("Кратні 3:", multiples_of_3)
print(f"Min: {min_val}; Max: {max_val}; Sum: {sum_val}; Average: {average_val:.2f}\n")


group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

common = group1 & group2
only_group1 = group1 - group2
only_group2 = group2 - group1
all_unique = group1 | group2

print("--- Завдання 2 ---")
print("Спільні:", ", ".join(common))
print("Tільки group1:", ", ".join(only_group1))
print("Tільки group2:", ", ".join(only_group2))
print("Усі:", ", ".join(sorted(all_unique)))
print()


print("--- Завдання 3 ---")

catalog = {
    "bread": 35,
    "milk": 48
}

catalog["cheese"] = 120
catalog["bread"] = 38
catalog["tea"] = 75

min_price = 40
max_price = 100

for product, current_price in catalog.items():
    if min_price <= current_price <= max_price:
        print(f"{product} — {current_price} грн")



print("--- Завдання 4 ---")
group_info = ('10-IT', '2026/2027')

journal = {
    "Anna": list((10, 11, 12, 9, 10)),
    "Ivan": list((8, 9, 10, 11, 9))
}

def add_student(name, grades):
    if len(grades) != 5:
        print(f"Помилка додавання {name}: має бути рівно 5 оцінок.")
        return
    for grade in grades:
        if not (1 <= grade <= 12):
            print(f"Помилка додавання {name}: оцінка {grade} поза діапазоном 1-12.")
            return
    journal[name] = grades

add_student("Olha", list((11, 12, 11, 10, 12)))

print(f"{group_info[0]} — {group_info[1]}")
for name, grades in journal.items():
    avg = sum(grades) / len(grades)
    print(f"{name} — {avg:.1f}")

best_name = ""
best_average = 0
ratings = []

for name, grades in journal.items():
    avg = sum(grades) / len(grades)
    ratings.append((name, avg))
    if avg > best_average:
        best_average = avg
        best_name = name

print(f"Найкращий результат: {best_name} — {best_average:.1f}")

ratings.sort(key=lambda x: x[1], reverse=True)
print("\nРейтинг групи:")
for place, (name, avg) in enumerate(ratings, 1):
    print(f"{place}. {name}: {avg:.2f}")