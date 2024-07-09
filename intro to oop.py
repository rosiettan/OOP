import logging
logger = logging.getLogger(__name__)


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.experience = 0

    # For printing self object __str__
    def __repr__(self):
        return f"A student with name {self.name} " \
               f"of age {self.age} has experience {self.experience}"

    def grow(self):
        self.age += 1

    def work(self, hours: int):
        self.experience += hours


students: list[Student] = list()

students.append(
    Student(name="John", age=16)
)
students.append(
    Student(name="Bill", age=17)
)

for student in students:
    for i in range(5):
        student.work(10)

print(students)


# student1 = Student(name="Bill", age=16)
# print(student1)
# logger.info(student1)