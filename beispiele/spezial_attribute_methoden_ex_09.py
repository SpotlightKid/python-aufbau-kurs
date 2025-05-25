class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __contains__(self, item):
        return self.start <= item < self.stop

r = MyRange(1, 5)
print(3 in r)   # Output: True
print(6 in r)   # Output: False
