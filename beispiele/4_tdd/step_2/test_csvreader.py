def test_init_separator():
    from csvreader import CSVReader
    parser = CSVReader([], separator=";")
    assert parser.separator == ";"
    assert parser.row_factory == None
    assert parser.fileobj == []
