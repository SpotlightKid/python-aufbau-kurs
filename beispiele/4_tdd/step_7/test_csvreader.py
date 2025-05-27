from dataclasses import dataclass
from csvreader import CSVReader

def test_from_file():
    with open("data.csv", "w") as csv:
        csv.write("a,b,c\n1,2,3\n")
    
    with open("data.csv") as csv:
        parser = CSVReader(csv)
        result = list(parser)
        assert result == [["a", "b", "c"], ["1", "2", "3"]]

def test_from_file_semicolon():
    with open("data.csv", "w") as csv:
        csv.write("a;b;c\n1;2;3\n")
    
    with open("data.csv") as csv:
        parser = CSVReader(csv, ";", tuple)
        result = list(parser)
        assert result == [("a", "b", "c"), ("1", "2", "3")]

def test_from_file_dataclass():
    @dataclass
    class Row:
        a: str
        b: str
        c: str
    
        @classmethod
        def fromlist(cls, lst):
            return cls(*lst)

    with open("data.csv", "w") as csv:
        csv.write("a;b;c\n1;2;3\n")

    with open("data.csv") as csv:
        parser = CSVReader(csv, ";", Row.fromlist)
        result = list(parser)
        assert isinstance(result[0], Row)
        assert result[0].a == 'a'
        assert result[0].b == 'b'
        assert result[0].c == 'c'
