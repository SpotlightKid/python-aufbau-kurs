class A:
    def action(self):
        print("A.action start")
        super().action()
        print("A.action end")

class B:
    def action(self):
        print("B.action start")
        super().action()
        print("B.action end")

class C:
    def action(self):
        print("C.action start")
        # No super() here, last in chain
        print("C.action end")

class D(A, B, C):
    def action(self):
        print("D.action start")
        super().action()
        print("D.action end")

# Usage
d = D()
d.action()

# Ausgabe:
# D.action start
# A.action start
# B.action start
# C.action start
# C.action end
# B.action end
# A.action end
# D.action end
