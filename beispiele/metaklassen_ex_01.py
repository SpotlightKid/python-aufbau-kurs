class UpperAttrMeta(type):
    """Metaclass that makes class attributes uppercase."""

    def __new__(metaklass, name, baseclasses, members):
        uppercase_attrs = {}
        for name, value in members.items():
            if not name.startswith('__'):
                uppercase_attrs[name.upper()] = value
            else:
                uppercase_attrs[name] = value
        return super().__new__(metaklass, name, baseclasses, uppercase_attrs)


class MyClass(metaclass=UpperAttrMeta):
    foo = 'bar'

    def hello(self):
        return "hello"


# Usage
obj = MyClass()
print(hasattr(obj, 'foo'))   # Output: False
print(hasattr(obj, 'FOO'))   # Output: True
print(obj.FOO)               # Output: bar
