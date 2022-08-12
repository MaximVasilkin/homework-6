class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def rate_lecture(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
				and course in self.courses_in_progress \
				and 1 <= grade <= 10:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'

	def __avg_grade(self):
		self.list_grades = [grade for grades in self.grades.values() for grade in grades]
		if self.list_grades:
			self.average_grade = sum(self.list_grades) / len(self.list_grades)
			return self.average_grade

	def __check_other(self, other):
		if not isinstance(other, Student):
			print('Сравнивать можно только студентов')
			return False
		else:
			return True

	def __str__(self):
		return (f'Имя: {self.name} \nФамилия: {self.surname}'
				f'\nСредняя оценка: {self.__avg_grade()}'
				f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
				f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

	def __gt__(self, other):
		if self.__check_other(other):
			return self.__avg_grade() > other.__avg_grade()

	def __eq__(self, other):
		if self.__check_other(other):
			return self.__avg_grade() == other.__avg_grade()

	def __le__(self, other):
		if self.__check_other(other):
			return self.__avg_grade() <= other.__avg_grade()


class Mentor:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses_attached = []


class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.grades = {}

	def __avg_grade(self):
		self.list_grades = [grade for grades in self.grades.values() for grade in grades]
		if self.list_grades:
			self.average_grade = sum(self.list_grades) / len(self.list_grades)
			return self.average_grade

	def __check_other(self, other):
		if not isinstance(other, Lecturer):
			print('Сравнивать можно только лекторов')
			return False
		else:
			return True

	def __str__(self):
		return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {self.__avg_grade()}'

	def __gt__(self, other):
		if self.__check_other(other):
			return self.__avg_grade() > other.__avg_grade()

	def __eq__(self, other):
		if self.__check_other(other):
			return self.__avg_grade() == other.__avg_grade()

	def __le__(self, other):
		if self.__check_other(other):
			return self.__avg_grade() <= other.__avg_grade()


class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached \
				and course in student.courses_in_progress \
				and 1 <= grade <= 10:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'

	def __str__(self):
		return f'Имя: {self.name} \nФамилия: {self.surname}'


student1 = Student('ivan', 'ivanov', 'm')
student1.courses_in_progress += ['python', 'some_course']
student1.finished_courses += ['english', 'spain']

student2 = Student('petr', 'petrov', 'm')
student2.courses_in_progress += ['git']

reviewer = Reviewer('Re', 'Viewer')
reviewer.courses_attached += ['python', 'git']
reviewer.rate_hw(student1, 'python', 2)
reviewer.rate_hw(student1, 'python', 6)
reviewer.rate_hw(student2, 'git', 9)
reviewer.rate_hw(student2, 'git', 6)

reviewer2 = Reviewer('Андрей', 'Вьюверов')
reviewer2.courses_attached += ['python', 'git']

lecturer = Lecturer('n', 'm')
lecturer.courses_attached += ['python', 'git']

student1.rate_lecture(lecturer, 'python', 7)
student2.rate_lecture(lecturer, 'git', 3)

lecturer3 = Lecturer('Test', 'Try')
lecturer3.courses_attached += ['python', 'git']

student1.rate_lecture(lecturer3, 'python', 4)
student2.rate_lecture(lecturer3, 'git', 2)

lecturer2 = Lecturer('Lec', 'Thor')
lecturer2.courses_attached += ['python', 'git']

student1.rate_lecture(lecturer2, 'git', 10)
student1.rate_lecture(lecturer2, 'python', 8)
student2.rate_lecture(lecturer2, 'git', 9)

print(dir(Student), dir(Lecturer), dir(Reviewer))

student3 = Student('semen', 'semenov', 'm')
student3.courses_in_progress += ['python']

reviewer2.rate_hw(student3, 'python', 10)
reviewer2.rate_hw(student3, 'python', 10)
reviewer2.rate_hw(student3, 'python', 9)


def avg_course_grade_students(students, course):
	if all([isinstance(item, Student) for item in students]):
		avg_course_grade = []
		for student in students:
			if course in student.grades:
				avg_course_grade += student.grades[course]
		if avg_course_grade:
			return sum(avg_course_grade) / len(avg_course_grade)
	else:
		return 'Ошибка! Кто-то не студент!'


def avg_course_grade_lecturer(lecturers, course):
	if all([isinstance(item, Lecturer) for item in lecturers]):
		avg_course_grade = []
		for lecturer in lecturers:
			if course in lecturer.grades:
				avg_course_grade += lecturer.grades[course]
		if avg_course_grade:
			return sum(avg_course_grade) / len(avg_course_grade)
	else:
		return 'Ошибка! Кто-то не Лектор!'
