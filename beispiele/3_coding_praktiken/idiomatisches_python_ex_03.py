# Statt:
i = 0
for item in items:
    print(i, item)
    i += 1

# Besser:
for i, item in enumerate(items):
    print(i, item)
