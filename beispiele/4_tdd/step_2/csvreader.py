class CSVReader:
    def __init__(self, fileobj, separator=",", row_factory=None):
        self.fileobj = fileobj
        self.separator = separator
        self.row_factory = row_factory
