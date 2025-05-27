def test_parse_lines():
    from csvreader import CSVReader
    lines = ["a,b,c", "1,2,3"]
    parser = CSVReader(iter(lines))
    result = list(parser)
    assert result == [["a", "b", "c"], ["1", "2", "3"]]
