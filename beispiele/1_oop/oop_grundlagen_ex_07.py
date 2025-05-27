s = "Hallo, {}"
print(s.format("Welt"))

s = "{}, {}"
print(s.format("Guten Tag", "Welt"))

s = "{name}, {grussformel}"
print(s.format(grussformel="Guten Tag", name="Welt"))

grussformel="Guten Tag"
name="Welt"
print(f"{name}, {grussformel}")


def sagehallo(name):
    # 'grussformel' ist eine globale variable!
    print(f"{grussformel}, {name}")

sagehallo("Welt")
