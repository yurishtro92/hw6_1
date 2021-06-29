class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):  # добавлен метод выставления оценки лектору
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # добавлен дочерний класс лектор, с дополнительным атрибутом grades
    def __init__(self, name, surname):
        super().__init__(name, surname)  # вернули родительскому классу его атрибуты
        self.grades = {}  # и добавили новый атрибут grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('AweSome', 'Buddy')
cool_reviewer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'gender')
best_student.courses_in_progress += ['Python']

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print('Reviewer:', cool_reviewer.name, cool_reviewer.surname)
print('Student`s grades:', best_student.name, best_student.surname, best_student.grades)
print('Lecturer`s grades:', cool_lecturer.name, cool_lecturer.surname, cool_lecturer.grades)