class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")

g = Greeter()
g("Alice")  # Output: Hello, Alice!
