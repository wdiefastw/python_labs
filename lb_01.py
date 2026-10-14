#1.1 Завдання
num = int(input("Введіть ціле число: "))
if num % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

#1.2 Завдання
age = int(input("Введіть свій вік: "))
if age >= 18:
    print("Ви повнолітні!")
else:
    print("Ви неповнолітні!")

#1.3 Завдання
import math
radius = float(input("Введіть радіус кола: "))
area = math.pi * (radius**2)
length = 2 * math.pi * radius
print(f"Площа круга: {round(area, 2)}")
print(f"Довжина круга:  {round(length, 2)}")

#1.4 Завдання
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

if a > b:
    print("Більше число: ", a)
elif b > a:
    print("Більше число: ", b)
elif a == b:
    print("Числа рівні!")

#2 Завдання
x, y = map(float, input("Введіть координати X та Y через пробіл: ").split())

if x > 0 and y > 0:
    print("Точка належить I чверті")

elif x < 0 and y > 0:
    print("Точка належить II чверті")

elif x < 0 and y < 0:
    print("Точка належить III чверті")

elif x > 0 and y < 0:
    print("Точка належить IV чверті")

else:
    print("Точка лежить на початку відліку")

#3 Завдання
age = int(input("Введіть вік людини від 0 до 120: "))

if 5 <= age % 100 <= 20:
    word = "років"

elif age % 10 == 1:
    word = "рік"

elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
    word = "роки"

else:
    word = "років"

print(age, word)

#4 Завдання
N = int(input("Введіть кількість поїздок: "))
k = int(input("Введіть кількість квитків у пачці: "))
p1 = int(input("Введіть вартість одного квитка: "))
p2 = int(input("Введіть вартість пачки квитків: "))

packs = N // k
remainder = N % k
cost1 = N * p1
cost2 = (packs * p2) + (remainder * p1)
cost3 = (packs + 1) * p2

min_cost = min(cost1, cost2, cost3)

print("Найменша сума:", min_cost)
