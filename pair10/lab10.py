import os

# Завдання 1
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Ім'я: {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        return f"Учень: {self.name}, група: {self.group}"


student1 = Student("Anna Ivanenko", "IT-17")
student2 = Student("Ivan Petrov", "IT-18")

print(student1.info())
print(student2.info())

# Завдання 2
class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Ім'я: {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f"Учень: {self.name}, група: {self.group}"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f"Викладач: {self.name}, предмет: {self.subject}"


teacher = Teacher("Olena Kovalenko", "Python")

people = [
    Person("Ivan Komarov"),
    Student("Anna Ivanenko", "IT-10"),
    Student("Oleh Petrenko", "IT-17"),
    teacher
]

for person in people:
    print(person.info())


# Завдання 3
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        for existing_student in self.students:
            if existing_student.name == student.name:
                return
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return

    def show_students(self):
        print(f"Курс: {self.title}")
        print(self.teacher.info())
        print("Студенти:")
        for number, student in enumerate(self.students, 1):
            print(f"{number}. {student.info()}")


course = Course("Python", teacher)
course.add_student(Student("Anna Ivanenko", "IT-10"))
course.add_student(Student("Oleh Petrenko", "IT-17"))
course.add_student(Student("Maria Bondarenko", "IT-17"))
course.add_student(Student("Andrii Shevchenko", "IT-10"))
course.add_student(Student("Anna Ivanenko", "IT-10"))
course.remove_student("Oleh Petrenko")
course.show_students()



# Завдання 4
def main():
    main_teacher = Teacher("Olena Kovalenko", "Python")
    course = Course("Python", main_teacher)
    course.load_from_file()

    while True:
        print("\n--- Меню ---")
        print("1 — показати курс")
        print("2 — додати студента")
        print("3 — видалити студента")
        print("4 — знайти студента")
        print("5 — виставити оцінку")
        print("6 — показати рейтинг")
        print("7 — зберегти дані")
        print("0 — вихід")
        
        choice = input("Ваш вибір: ").strip()
        
        if choice == "1":
            course.show_students()
        elif choice == "2":
            name = input("ПІБ студента: ").strip()
            group = input("Група студента: ").strip()
            if name and group:
                new_student = Student(name, group)
                if course.add_student(new_student):
                    print("Студента успішно додано.")
                else:
                    print("Студент із таким ім'ям вже є на курсі.")
        elif choice == "3":
            name = input("ПІБ для видалення: ").strip()
            if course.remove_student(name):
                print("Студента видалено.")
            else:
                print("Учня не знайдено.")
        elif choice == "4":
            name = input("ПІБ для пошуку: ").strip()
            student = course.find_student(name)
            if student:
                print(student.info())
            else:
                print("Учня не знайдено.")
        elif choice == "5":
            name = input("ПІБ студента: ").strip()
            student = course.find_student(name)
            if student:
                try:
                    grade = int(input("Введіть оцінку (1-12): "))
                    if course.add_grade_to_student(name, grade):
                        print("Оцінку виставлено.")
                    else:
                        print("Неправильна оцінка! Має бути від 1 до 12.")
                except ValueError:
                    pass
            else:
                print("Учня не знайдено.")
        elif choice == "6":
            course.show_rating()
        elif choice == "7":
            if course.save_to_file():
                print("Дані збережено.")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
