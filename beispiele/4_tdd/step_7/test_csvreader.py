def test_from_file(tmp_path):
    from csvreader import CSVReader
    with open("data.csv", "w") as csv:
        csv.write("a,b,c\n1,2,3\n")
    
    with open("data.csv") as csv:
        parser = CSVReader(csv)
        result = list(parser)
        assert result == [["a", "b", "c"], ["1", "2", "3"]]
