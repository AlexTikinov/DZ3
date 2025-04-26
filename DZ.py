class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lec(self, lec, course, grade):
        if isinstance(lec, Lecturer) and course in lec.courses_attached and course in self.courses_in_progress:
           if course in lec.grades:
                lec.grades[course] += [grade]
           else:
                lec.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {srednee(self)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
    def __eq__(self, other): return srednee(self) == srednee(other)
    def __gt__(self, other): return srednee(self) > srednee(other)
    def __lt__(self, other): return srednee(self) < srednee(other)
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades={}
    def __str__(self):
        return (f"Имя: {self.name}\n"
        f"Фамилия: {self.surname}\n"
        f"Средняя оценка за лекции: {srednee(self)}")
    def __eq__(self, other): return srednee(self) == srednee(other)
    def __gt__(self, other): return srednee(self) > srednee(other)
    def __lt__(self, other): return srednee(self) < srednee(other)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
           if course in student.grades:
                student.grades[course] += [grade]
           else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f"Имя: {self.name}\n"
        f"Фамилия: {self.surname}")

def comp(ekz, course): #Считаем среднее значение по оценкам за курс
    aver=0
    if isinstance(ekz, Lecturer) and course in ekz.courses_attached:
        aver = sum(ekz.grades[course])/len(ekz.grades[course])
        return round(aver, 2)
    elif isinstance(ekz, Student) and course in ekz.courses_in_progress:
        aver = sum(ekz.grades[course])/len(ekz.grades[course])
        return round(aver, 2)
    else:
        print('Запрос некорректен')
def srednee(ekz):  #Считаем общее среднее значение для лектора или студента по всем оченкам
    ob = []
    for gr in ekz.grades.values():
        ob += gr
    avrg= sum(ob)/len(ob)
    return round(avrg, 2)
def aver_stu(spisok, course): #Выводим список студентов по списку для курса
    k=0
    for sp in spisok:
        if  isinstance(sp, Student) and course in sp.courses_in_progress:
            print (f'{sp.name} {sp.surname} имеет средний балл {comp(sp, course)} по курсу {course}')
            k+=1
        else:
            continue
    if k==0:
        print("По Вашему запросу ничего не найдено")
def aver_lec(spisok, course): #Выводим список лекторов по списку для курса
    k=0
    for sp in spisok:
        if  isinstance(sp, Lecturer) and course in sp.courses_attached:
            print (f'{sp.name} {sp.surname} имеет средний балл {comp(sp, course)} по курсу {course}')
            k+=1
        else:
            continue
    if k==0:
        print("По Вашему запросу ничего не найдено")
    
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'PHP', '1C']
student1.finished_courses += ['Java']
student2 = Student('James', 'Leon', 'male')
student2.courses_in_progress += ['Python', 'Java', 'Go']
student2.finished_courses += ['C++']

lecturer1 = Lecturer('Monica', 'Green')
lecturer1.courses_attached += ['Python', 'PHP', '1C']
lecturer2 = Lecturer('Carla', 'Mona')
lecturer2.courses_attached += ['Python', 'Go', 'Java']

revuer1 = Reviewer('Aex', 'Stone')
revuer1.courses_attached += ['Python', 'PHP', 'Go']
revuer2 = Reviewer('Mary', 'Bone')
revuer2.courses_attached += ['Python', 'Java', '1C', 'C++']

student1.rate_lec(lecturer1, 'Python', 1)
student1.rate_lec(lecturer1, 'Python', 4)
student2.rate_lec(lecturer1, 'Python', 6)
student1.rate_lec(lecturer1, 'PHP', 6)
student1.rate_lec(lecturer1, 'PHP', 8)
student1.rate_lec(lecturer1, 'PHP', 7)
student1.rate_lec(lecturer1, '1C', 3)
student1.rate_lec(lecturer1, '1C', 1)
student1.rate_lec(lecturer1, '1C', 9)

student1.rate_lec(lecturer2, 'Python', 5)
student2.rate_lec(lecturer2, 'Python', 5)
student2.rate_lec(lecturer2, 'Python', 6)
student2.rate_lec(lecturer2, 'Java', 8)
student2.rate_lec(lecturer2, 'Java', 6)
student2.rate_lec(lecturer2, 'Java', 8)
student2.rate_lec(lecturer2, 'Go', 4)
student2.rate_lec(lecturer2, 'Go', 3)
student2.rate_lec(lecturer2, 'Go', 2)

revuer1.rate_hw(student1, 'Python', 1)
revuer1.rate_hw(student1, 'Python', 2)
revuer2.rate_hw(student1, 'Python', 7)
revuer1.rate_hw(student1, 'PHP', 5)
revuer1.rate_hw(student1, 'PHP', 4)
revuer1.rate_hw(student1, 'PHP', 9)
revuer2.rate_hw(student1, '1C', 6)
revuer2.rate_hw(student1, '1C', 8)
revuer2.rate_hw(student1, '1C', 8)

revuer1.rate_hw(student2, 'Python', 6)
revuer2.rate_hw(student2, 'Python', 9)
revuer2.rate_hw(student2, 'Python', 7)
revuer2.rate_hw(student2, 'Java', 3)
revuer2.rate_hw(student2, 'Java', 9)
revuer2.rate_hw(student2, 'Java', 9)
revuer1.rate_hw(student2, 'Go', 5)
revuer1.rate_hw(student2, 'Go', 2)
revuer1.rate_hw(student2, 'Go', 7)

print(student1)
print(revuer1)
print(lecturer1)

print(student1 == student2)
print(student1 > student2)
print(student1 < student2)

print(lecturer1 == lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)

print(comp(lecturer1, '1C'))
print(comp(student1, 'Python'))

stu = [student1, student2]
print(aver_stu(stu, 'Python'))
lec = [lecturer2, lecturer1]
print(aver_lec(lec, '1C'))