from lab_python_oop.person import Person


class Student(Person):
    name = "Студент"

    def __init__(self, fio, age, gender, scholarship):
        super().__init__(fio, age, gender)
        self.scholarship = scholarship  

    def income(self):
        return self.scholarship
