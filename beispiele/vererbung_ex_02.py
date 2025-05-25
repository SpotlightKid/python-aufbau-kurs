class Person:

    def __init__(self, name="", age=0, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person: name={self.name} ({self.age})"


class Employee(Person):

    def __init__(self, name="", age=0, gender=None, employee_id=None, salary=0):
        super().__init__(name=name, age=age, gender=gender)
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return f"Employee: name={self.name} employee_id={self.employee_id}"


# Usage
person = Person("Alice", 30, "female")
print(person)  # Output: Person: name=Alice (30)

employee = Employee("Bob", 40, "male", employee_id="E123", salary=50000)
print(employee)  # Output: Employee: name=Bob employee_id=E123
