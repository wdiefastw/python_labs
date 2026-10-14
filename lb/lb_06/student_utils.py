import random
import statistics

def generate_grades(count):
    return [random.randint(1, 12) for _ in range(count)]

def average_grade(grades):
    if not grades:
        return 0.0
    return statistics.mean(grades)

def get_level(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"
