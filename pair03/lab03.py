
# Завдання 1

text = input("Введіть текст: ")

letter_count = 0
digit_count = 0
space_count = 0
vowel_count = 0

vowels = "аеєиіїоуюяaeiou"

for char in text:
    if char.isalpha():
        letter_count += 1

    if char.isdigit():
        digit_count += 1

    if char == " ":
        space_count += 1

    if char.lower() in vowels:
        vowel_count += 1

words = text.split()

print("Символів:", len(text))
print("Літер:", letter_count)
print("Цифр:", digit_count)
print("Пробілів:", space_count)
print("Голосних:", vowel_count)
print("Слів:", len(words))


# Завдання 2

full_name = input("\nВведіть прізвище, ім'я та по батькові: ")

parts = full_name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    name = parts[1].capitalize()
    patronymic = parts[2].capitalize()

    result = surname + " " + name[0] + "." + patronymic[0] + "."
    print("Результат:", result)
else:
    print("Помилка: потрібно ввести рівно три слова.")


# Завдання 3

text1 = input("\nВведіть перший рядок: ")
text2 = input("Введіть другий рядок: ")

a = text1.lower().replace(" ", "")
b = text2.lower().replace(" ", "")

print("Перший нормалізований рядок:", a)
print("Другий нормалізований рядок:", b)

if sorted(a) == sorted(b):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")


# Завдання 4

sentence = input("\nВведіть речення: ")

words = sentence.split()

if len(words) > 0:
    lengths = []

    for word in words:
        clean_word = word.strip(".,!?;:()\"'")
        lengths.append(len(clean_word))

    max_length = max(lengths)
    min_length = min(lengths)

    longest_words = []
    shortest_words = []
    unique_words = []

    for i, word in enumerate(words):
        clean_word = word.strip(".,!?;:()\"'")

        if len(clean_word) == max_length:
            if clean_word not in longest_words:
                longest_words.append(clean_word)

        if len(clean_word) == min_length:
            if clean_word not in shortest_words:
                shortest_words.append(clean_word)

        normalized = clean_word.lower()

        if normalized not in unique_words:
            unique_words.append(normalized)


    print("Найдовші:", ", ".join(longest_words))
    print("Найкоротші:", ", ".join(shortest_words))
    print("Унікальних слів:", len(unique_words))

    old_word = input("Введіть слово для заміни: ")
    new_word = input("Введіть нове слово: ")

    new_sentence = sentence.replace(old_word, new_word)

    print("Після заміни:", new_sentence)
else:
    print("Речення не містить слів.")
