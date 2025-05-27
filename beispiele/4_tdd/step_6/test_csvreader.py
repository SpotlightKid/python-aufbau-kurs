def test_row_factory():
    from csvreader import CSVReader
    lines = ["a,b,c", "1,2,3"]
    parser = CSVReader(iter(lines), row_factory=tuple)
    result = list(parser)
    assert result == [("a", "b", "c"), ("1", "2", "3")]
