def quack(animal):
    animal.quack()  # Funktioniert für alle, die eine quack()-Methode haben

class Duck:
    def quack(self):
        print("Quack!")

class FakeDuck:
    def quack(self):
        print("I'm pretending!")
