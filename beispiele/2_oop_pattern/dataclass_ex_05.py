@dataclass(frozen=True)
class Person:
    name: str
    age: int

p = Person("Carol", 22)
# p.age = 23  # Raises error (cannot assign to field 'age')
