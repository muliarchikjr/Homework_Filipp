
class Student:

    def __init__(self, surname, name, group, grades):

        self.surname = surname
        self.name = name
        self.group = group
        self.grades = grades if grades else []

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def add_grade(self, *another_grades):

        self.grades.extend(grade for grade in another_grades if 1 <= grade <= 10)

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

students = [
    Student("Иванов", "Иван", "9А", [8, 9, 10, 7, 8]),
    Student("Петров", "Петр", "9Б", [6, 7, 5, 6, 7]),
    Student("Сидоров", "Алексей", "9В", [9, 10, 9, 8, 10]),
    Student("Кузнецов", "Дмитрий", "9Г", [4, 5, 6, 5, 6]),
    Student("Смирнов", "Николай", "9Д", [10, 9, 10, 9, 10])
]

print("Студенты по возрастанию среднего балла:")
for student in sorted(students):
    print(student)

print("\nСтуденты по убыванию среднего балла:")
for student in sorted(students, reverse=True):
    print(student)

print("\nСтуденты со средним баллом выше 8:")
for student in students:
    if student.average_grade() > 8:
        print(student)





