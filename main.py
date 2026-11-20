from tabulate import tabulate

from lab_python_oop.student import Student
from lab_python_oop.teacher import Teacher
from lab_python_oop.head import Head


def main():
    student = Student("Иванов Иван Иванович", 20, "м", 5000)
    teacher = Teacher("Петрова Мария Сергеевна", 45, "ж", 60000, 15)
    head = Head("Сидоров Алексей Петрович", 55, "м", 80000, 25)

    print(student)
    print(teacher)
    print(head)
    print()

    table = [
        [student.get_name(), student.fio, student.income()],
        [teacher.get_name(), teacher.fio, teacher.income()],
        [head.get_name(), head.fio, head.income()],
    ]
    headers = ["Должность", "ФИО", "Средний доход, руб."]

    print(tabulate(table, headers=headers, floatfmt=".2f"))


if __name__ == "__main__":
    main()
