class Employee:
    def __init__(self, name="", gehalt=0, skills=[]):
        self.name = name
        self.gehalt = gehalt

        if skills is None:
            self.skills = []
        else:
            self.skills = skills

employee4 = Employee("Joe Doe", 2000, [])
print(type(employee4))
print(employee4.name)
print(employee4.gehalt)
print(employee4.skills)

employee5 = Employee("Jane Oh", 3000, ["marketing"])
print(employee5.name)
print(employee5.gehalt)
print(employee5.skills)
