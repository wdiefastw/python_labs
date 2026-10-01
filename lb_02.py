# Завдання 1
n = int(input("Введіть натуральне число N: "))
total_sum = 0
count = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i
        count += 1

print(f"Кількість: {count}")
print(f"Сума: {total_sum}")

if count > 0:
    average = total_sum / count
    print(f"Середнє: {average:.2f}")
else:
    print("Чисел, кратних 3 або 5, у цьому діапазоні немає.")



# Завдання 2
n = int(input("Введіть натуральне число N: "))
temp = n
if temp == 0:
    count = 1
    total_sum = 0
    max_digit = 0
    min_digit = 0
else:
    count = 0
    total_sum = 0
    max_digit = -1
    min_digit = 10

    while temp > 0:
        digit = temp % 10
        
        count += 1
        total_sum += digit
        
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
            
        temp //= 10

print(f"Кількість цифр: {count}")
print(f"Сума цифр: {total_sum}")
print(f"Найбільша цифра: {max_digit}")
print(f"Найменша цифра: {min_digit}")



# Завдання 3

n = int(input("Введіть натуральне число N: "))

for i in range(1, n + 1):
    temp = i
    divisible_by_all = True
    while temp > 0:
        digit = temp % 10
        if digit == 0 or i % digit != 0:
            divisible_by_all = False
            break
            
        temp //= 10
    
    if divisible_by_all:
        print(i, end=" ")


# Завдання 4

width = int(input("Введіть ширину (width): "))
height = int(input("Введіть висоту (height): "))
border_char = input("Введіть символ контуру: ")
fill_char = input("Введіть символ внутрішньої частини: ")

if width < 3 or height < 3:
    print("Помилка: мінімальний розмір рамки — 3x3.")
else:
    for r in range(height):
        for c in range(width):
            if r == 0 or r == height - 1 or c == 0 or c == width - 1:
                print(border_char, end="")
            else:
                print(fill_char, end="")
        print()


#Додаткове завдання

size = int(input("Розмір трикутника = "))
if size <= 1:
    print("Помилка: розмір має бути більшим за 1")
else:
    for r in range(1, size + 1):
        for c in range(r):
            print("*", end="")
        print()
