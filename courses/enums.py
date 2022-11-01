from enum import Enum


class Languages(Enum):
    uzbek = 'uzbek'
    rus = 'rus'
    english = 'english'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)