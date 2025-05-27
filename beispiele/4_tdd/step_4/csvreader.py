class CSVReader:
    def __init__(self, fileobj, separator=",", row_factory=None):
        self.fileobj = fileobj
        self.separator = separator
        self.row_factory = row_factory
        self._iter = iter(self.fileobj)

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._iter)
        row = line.strip().split(self.separator)
        if self.row_factory:
            row = self.row_factory(row)
        return row
