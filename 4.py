
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
       self.finished_course.append(course_name) 

    def rate(self, lecturer, course, grade):
        for lecturer in Lecturer:
            count = 0
            if isinstance(lecturer, Lecturer) and course in Student.finished_courses and course in Student.courses_in_progress:
                 if course in Lecturer.grades:
                    lecturer.grades[course] += [grade] / len([grade])
                    count += 1
                    return round(lecturer.grades[course]/ count, 2)
                 else:
                      lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'    
    def __str__(self) :
        res1 = 'Имя: {}, Фамилия: {}, Средняя оценка за домашние задания: {}, Курсы в процессе изучения: {}, Завершенные курсы: {}'.format(self.name, self.surname, self.grades, self.courses_in_progress, self.finished_courses)
        return res1
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            
        return self.grades < other.grades

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname ): 
        self.finished_courses = []
        self.courses_in_progress = []  
        self.grades = {'course': 'grade'}  


    def __str__(self) :
        res2 = 'Имя: {}, Фамилия: {}, Средняя оценка за лекции: {},'.format(self.name, self.surname, self.grades)
        return res2
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
        
        return self.grades < other.grades


class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                 if course in student.grades:
                    student.grades[course] += [grade] / len([grade])
                    counter += 1
                    return round(student.grades[course]/ counter, 2)
                 else:
                    student.grades[course] = [grade]/ len([grade])
            else:
                return 'Ошибка'
    
    def __str__(self) :
        res3 = 'Имя: {}, Фамилия: {}'.format(self.name, self.surname)
        return res3




Reviewer('Some', 'Boddy')
some_student = Student('Anna', 'Ivanova', 'f')
reviewer1=Reviewer('Some', 'Boddy')
print(reviewer1)
print(some_student)

student1=Student('Ivan', 'Poll', 'm')
student2=Student('Sveta', 'Fohk', 'f')
student1.courses_in_progress += ['Phyton']
student1.finished_courses += ['Git']
student2.courses_in_progress += ['Phyton']
student2.finished_courses += ['Git']
student1.grades = 8
student2.grades = 10
print(student1 > student2)

lecturer1=Lecturer('Michail', 'Ivanov')
lecturer2=Lecturer('Was', 'Pit')
lecturer1.courses_in_progress += ['Phyton']
lecturer2.courses_in_progress += ['Git']

reviewer1.rate_hw(student1, 'Phyton', 9)
reviewer1.rate_hw(student2, 'Phyton', 7)
student1.rate(lecturer1, 'Phyton', 10)
student2.rate(lecturer1, 'Phyton', 8)



