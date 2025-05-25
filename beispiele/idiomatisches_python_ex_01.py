# Statt:
squares = []
for x in range(10):
    squares.append(x * x)

# Schöner (meistens):
squares = [x * x for x in range(10)]
