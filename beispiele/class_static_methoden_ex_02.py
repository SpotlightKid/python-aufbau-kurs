class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_hex(cls, hexstr):
        """Create instance from CSS-like hex color string (e.g. '#FFAA00')."""
        hexstr = hexstr.lstrip('#')
        red = int(hexstr[0:2], 16)
        green = int(hexstr[2:4], 16)
        blue = int(hexstr[4:6], 16)
        return cls(red, green, blue)

# Instanziierung mit Standard-Konstruktor
c1 = Color(128, 200, 255)
print(c1.red, c1.green, c1.blue)  # Ausgabe: 128 200 255

# Instanziierung mit Factory-Methode
c2 = Color.from_hex("#FFAA00")
print(c2.red, c2.green, c2.blue)  # Ausgabe: 255 170 0
