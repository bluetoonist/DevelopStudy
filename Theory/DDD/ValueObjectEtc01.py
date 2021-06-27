from typing import Type
from functools import total_ordering
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    age: int


class Human(object):
    def __init__(self, user: Person):
        # Data Validation

        if len(user.name) < 3:
            raise ValueError(f"{user.name} is less 3 length ")

        self._name = user.name
        self._age = user.age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError(f"{other} Is Miss Type")
        return True


if __name__ == '__main__':
    user01 = Person("jian", 19)
    user02 = Person("ji-in", 19)

    print(Human(user01) == Human(user02))
