class Employee:
    def __init__(self, name="", gehalt=0, skills=[]):
        self.name = name
        self.gehalt = gehalt

        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def set_gehalt(self, neues_gehalt):
        if not isinstance(neues_gehalt, int):
            raise TypeError("gehalt muss ein Integer sein")
        if neues_gehalt < 4000:
            self.gehalt = neues_gehalt
        else:
            raise ValueError("Zu hohes gehalt!")


employee8 = Employee()
# Ok
employee8.gehalt = 5000
# Auch ok (aber unsinnig!)
employee8.gehalt = "feuchter Händedruck"

print(employee8.gehalt)
# ValueError!
employee8.set_gehalt(4000)
# TypeError!
employee8.set_gehalt("feuchter Händedruck")
