@dataclass
class Person:
    name: str
    age: int = 0

p = Person("Bob")
print(p)  # Person(name='Bob', age=0)
