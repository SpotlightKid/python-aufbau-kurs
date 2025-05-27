import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.6f} seconds.")
        return result
    return wrapper

@timeit
def slow_add(a, b):
    """Adds two numbers with artificial delay."""
    time.sleep(0.5)
    return a + b

slow_add(4, 5)
