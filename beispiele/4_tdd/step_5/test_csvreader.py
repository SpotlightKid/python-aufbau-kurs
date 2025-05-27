def test_different_separator():
    from csvreader import CSVReader
    lines = ["a;b;c", "1;2;3"]
    parser = CSVReader(iter(lines), separator=";")
    result = list(parser)
    assert result == [["a", "b", "c"], ["1", "2", "3"]]
