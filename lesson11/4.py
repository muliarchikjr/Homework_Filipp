
with open('students_grades.txt', 'r', encoding='utf-8') as file:
    dictionary = {}
    for line in file.readlines():
        elements = line.split(',')

        klass = elements[1]
        student = elements[0]
        subject = elements[2].split()[0], grades = elements[2].split()[1]

        if klass not in dictionary:
            pass
