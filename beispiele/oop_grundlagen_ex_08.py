class Employee:
    def __init__(self, name="", gehalt=0, skills=[]):
        self.name = name
        self.gehalt = gehalt

        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def __str__(self):
        s  = [f"Employee '{self.name}'"]
        s.append(f"    gehalt: {self.gehalt}")
        s.append(f"    skills:")
        for skill in self.skills:
            s.append(f"        - {skill}")
        return "\n".join(s)
