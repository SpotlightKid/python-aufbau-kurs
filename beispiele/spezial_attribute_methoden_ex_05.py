class MyList:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

ml = MyList([1, 2, 3])
print(len(ml))      # Output: 3
print(ml[1])        # Output: 2
ml[1] = 99
print(ml[1])        # Output: 99
