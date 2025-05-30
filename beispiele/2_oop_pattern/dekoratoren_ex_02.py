import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add.__name__)      # Output: add
print(add.__doc__)       # Output: Adds two numbers.
