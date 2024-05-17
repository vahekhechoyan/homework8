import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' executed in {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def example_task(x, y):
    time.sleep(1)
    return x + y

if __name__ == "__main__":
    example_task(5, 10)
