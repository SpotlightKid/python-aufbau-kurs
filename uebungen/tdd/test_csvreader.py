import csvreader

def test_csvreader_init():
    reader = csvreader.CSVReader()
    assert isinstance(reader, csvreader.CSVReader)

def test_csvreader_with_file():
    with open("data.csv") as fileobj:
        reader = csvreader.CSVReader(fileobj)
        row = next(reader)
        assert isinstance(row, list)
        assert isinstance(row[0], str)

