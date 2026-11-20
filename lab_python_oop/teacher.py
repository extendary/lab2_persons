from lab_python_oop.person import Person


class Teacher(Person):
    name = "Преподаватель"
    bonus = 0.01  

    def __init__(self, fio, age, gender, salary, experience):
        super().__init__(fio, age, gender)
        self.salary = salary          
        self.experience = experience  
    def income(self):
        return self.salary * (1 + self.bonus * self.experience)

    def __repr__(self):
        return "{}, стаж {} лет".format(super().__repr__(), self.experience)
