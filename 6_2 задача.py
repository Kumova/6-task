
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
        lecturer.grades[course] = 0
        counter = 0
        for lecturer in Lecturer:
            if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in Student.courses_in_progress:
                 if course in lecturer.grades:
                    lecturer.grades[course] += sum(lecturer["grade"]) / len(lecturer["grade"])
                    counter += 1
                    return round(lecturer.grades[course]/ counter, 2)
                 else:
                      lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'    
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
         

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __init__(self, course, grade):
        self.lecturer.grades[course] 
        

class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        student.grades[course] = 0
        counter = 0
        for student in Student:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                 if course in student.grades:
                    student.grades[course] += sum(student["grade"]) / len(student["grade"])
                    counter += 1
                    return round(student.grades[course]/ counter, 2)
                 else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
  

Anna = Student('Anna', 'Ivanova', 'f')
Ivan = Lecturer('phyton', 8)
Sergey = Reviewer('Sergey', 'Ivanov')


#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']
 
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
 
#print(best_student.grades)

