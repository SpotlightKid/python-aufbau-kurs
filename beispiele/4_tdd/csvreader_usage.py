from csvreader import CSVReader

with open("data.csv") as f:
    parser = CSVReader(f, separator=";", row_factory=tuple)
    for row in parser:
        print(row)

# Ausgabe:
# ('a', 'b', 'c')
# ('1', '2', '3')
