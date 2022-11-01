from enum import Enum


class UserRoles(Enum):
    director = 'director'
    manager = 'manager'
    teacher = 'teacher'
    student = 'student'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)

