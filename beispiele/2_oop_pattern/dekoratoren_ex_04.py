def log_with_level(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_level("INFO")
def add(a, b):
    return a + b

add(3, 4)
