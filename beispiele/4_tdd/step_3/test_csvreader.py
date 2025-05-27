def test_iterable():
    from csvreader import CSVReader
    parser = CSVReader([])
    assert hasattr(parser, "__iter__")
