from abc import ABC, abstractmethod


class Person(ABC):
    name = "Персона"

    def __init__(self, fio, age, gender):
        self.fio = fio
        self.age = age
        self.gender = gender

    @abstractmethod
    def income(self):
        pass

    @classmethod
    def get_name(cls):
        return cls.name

    def __repr__(self):
        return "{}: {}, возраст {}, пол {}".format(
            self.get_name(), self.fio, self.age, self.gender
        )
