"""PRACTICES/oops.py

10 basic OOP questions covering:
- Encapsulation
- Abstraction
- Polymorphism
- Inheritance

Run: python PRACTICES/oops.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# ------------------------- Encapsulation -------------------------

# Q1: Encapsulation - private attribute + validation
class Student:
    def __init__(self, name: str, age: int):
        self._name = name  # "private by convention"
        self._age = 0
        self.age = age  # use setter for validation

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def display(self) -> str:
        return f"{self._name} is {self._age} years old"


# Q2: Encapsulation - Bank account with safe balance operations
class BankAccount:
    def __init__(self, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount


# ------------------------- Abstraction -------------------------

# Q3: Abstraction - Abstract base class with abstract area()
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


# Q4: Abstraction - Shapes with abstract draw()
class Drawable(ABC):
    @abstractmethod
    def draw(self) -> str:
        raise NotImplementedError


class Line(Drawable):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def draw(self) -> str:
        return f"Line drawn from ({self.x1},{self.y1}) to ({self.x2},{self.y2})"


# ------------------------- Polymorphism -------------------------

# Q5: Polymorphism - same method name, different implementations
class Dog:
    def speak(self) -> str:
        return "Woof!"


class Cat:
    def speak(self) -> str:
        return "Meow!"


def polymorphic_speak(animal) -> str:
    # duck-typing: expects animal.speak()
    return animal.speak()


# Q6: Polymorphism - duck typing with any object that has talk()
class Robot:
    def talk(self) -> str:
        return "Beep boop"


class TalkerPerson:
    def talk(self) -> str:
        return "Hello!"



def make_it_talk(obj) -> str:
    return obj.talk()


# Q7: Polymorphism - special method overriding (__len__)
class Bag:
    def __init__(self, items: list[object] | None = None):
        self._items = items or []

    def __len__(self) -> int:
        return len(self._items)

    def add(self, item: object) -> None:
        self._items.append(item)


# ------------------------- Inheritance -------------------------

# Q8: Inheritance - single inheritance (Student extends Person)
class Person:
    def __init__(self, name: str):
        self.name = name

    def introduce(self) -> str:
        return f"Hi, I am {self.name}."


class Student2(Person):
    def __init__(self, name: str, roll_no: int):
        super().__init__(name)
        self.roll_no = roll_no

    def introduce(self) -> str:
        # method overriding
        return f"Hi, I am {self.name} (Roll: {self.roll_no})."


# Q9: Inheritance - multilevel (Grandparent -> Parent -> Child)
class Grandparent:
    def family(self) -> str:
        return "Grandparent"


class Parent(Grandparent):
    def family(self) -> str:
        return "Parent"


class Child(Parent):
    def family(self) -> str:
        return "Child"


# Q10: Inheritance - method overriding + super()
class AnimalBase:
    def sound(self) -> str:
        return "Some sound"


class Dog2(AnimalBase):
    def sound(self) -> str:
        return super().sound() + " -> Woof"


if __name__ == "__main__":
    # Q1
    s = Student("Abhinav", 20)
    print("Q1 Encapsulation:", s.display())

    # Q2
    acc = BankAccount(1000)
    acc.deposit(250)
    acc.withdraw(100)
    print("Q2 BankAccount balance:", acc.get_balance())

    # Q3
    r = Rectangle(5, 4)
    print("Q3 Abstraction (Rectangle area):", r.area())

    # Q4
    l = Line(0, 0, 3, 4)
    print("Q4 Abstraction (draw):", l.draw())

    # Q5
    print("Q5 Polymorphism speak:", polymorphic_speak(Dog()), polymorphic_speak(Cat()))

    # Q6
    # Q6: NOTE Person is redefined below for inheritance section; use a dedicated talker here.
    print("Q6 Duck typing talk:", make_it_talk(Robot()), make_it_talk(TalkerPerson()))

    # Q7
    b = Bag(["pen", "notebook"])
    b.add("pencil")
    print("Q7 __len__ polymorphism:", len(b))

    # Q8
    st = Student2("Rahul", 12)
    print("Q8 Inheritance override:", st.introduce())

    # Q9
    c = Child()
    print("Q9 Multilevel inheritance:", c.family())

    # Q10
    d = Dog2()
    print("Q10 super() overriding:", d.sound())

