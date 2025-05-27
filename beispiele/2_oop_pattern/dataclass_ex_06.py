from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    id: int = field(default=0, compare=False)

p1 = Person("Dave", 40, id=1)
p2 = Person("Dave", 40, id=2)
print(p1 == p2)  # True, da id nicht verglichen wird
