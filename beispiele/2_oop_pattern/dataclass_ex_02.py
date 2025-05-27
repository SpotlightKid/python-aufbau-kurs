from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(p)            # Person(name='Alice', age=30)
print(p.name)       # Alice
print(p.age)        # 30
