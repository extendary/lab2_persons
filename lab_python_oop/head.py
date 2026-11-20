from lab_python_oop.teacher import Teacher


class Head(Teacher):
    name = "Заведующий кафедрой"
    allowance = 20000  

    def income(self):
        return super().income() + self.allowance
