from functools import wraps

def error_handling_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in '{func.__name__}': {e}")
            raise
    return wrapper

@error_handling_decorator
def example_task(x, y):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x + y

if __name__ == "__main__":
    try:
        result = example_task(-1, 10)
    except Exception as e:
        print(f"Task failed with exception: {e}")
