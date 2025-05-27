def test_csvreader_exists():
    from csvreader import CSVReader
    parser = CSVReader([])
    assert parser is not None
