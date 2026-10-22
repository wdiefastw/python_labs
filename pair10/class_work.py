class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Name: {self.name}"

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name) #дає доступ до батьківського класу
        self.group = group
    def info(self):
        return f"Name: {self.name}, Group: {self.group}"

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f"Name: {self.name}, Subject: {self.subject}"

# person1 = Person("Olesia")
# student1 = Student("Liza", "10-IT")
# teacher1 = Teacher("Ivan", "IT")

people = [Person("Olesia"), Student("Liza", "10-IT"), Teacher("Ivan", "IT")]

for person in people:
    print(person.info())
person = Student("Liza", "10-IT")
print(isinstance(person, Person))