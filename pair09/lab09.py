#Завдання 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
        
    def area(self):
        return self.width * self.height

    def info(self):
        print(f'Розміри прямокутника {self.width}x{self.height}')
        print(f'S={self.area()}')
        print(f'P={self.perimeter()}')


rect = Rectangle(5, 10)
rect.info()


#Завдання 2
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        if not all(0 <= grade <= 12 for grade in self.grades):
            raise ValueError("Оцінки повинні бути в діапазоні від 0 до 12")

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print("ПІБ:", self.name)
        print("Оцінки:", self.grades)
        print("Середній:", round(self.average(), 2))

student = Student("Ivan Petrenko", [8, 10, 11])
student.info()

#Завдання 3
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        if not all(0 <= grade <= 12 for grade in self.grades):
            raise ValueError("Оцінки повинні бути в діапазоні від 0 до 12")

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print(f"{self.name} — {self.average():.2f}")


students = [
    Student("Anna", [10, 11, 12]),
    Student("Ivan", [8, 9, 10]),
    Student("Olha", [12, 12, 11]),
    Student("Petro", [10, 10, 9]),
    Student("Olena", [11, 12, 11])
]


for student in students:
    student.info()
print("...") 
max_avg_score = max(student.average() for student in students)
for student in students:
    if student.average() == max_avg_score:
        print(f"Найкращий результат: {student.name} — {student.average():.2f}")



#Завдання 4
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print(f"Помилка: сума поповнення повинна бути більшою за 0 (передано: {amount})")
            return
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            print(f"Помилка: сума списання повинна бути більшою за 0 (передано: {amount})")
            return
        if amount > self.balance:
            print(f"Помилка: недостатньо коштів для -{amount} (поточний баланс: {self.balance})")
            return
        self.balance -= amount

    def info(self):
        print(f"{self.owner}: баланс {self.balance}")

account1 = BankAccount("Ivan", 1000)
account1.deposit(500) 
account1.withdraw(300)
account1.withdraw(2000)

account2 = BankAccount("Olha", 700)
account2.withdraw(200)
account2.deposit(100)

print("\n--- Кінцевий результат ---")

account1.info()
account2.info()
