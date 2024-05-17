import time
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            print(f"'{func.__name__}' executed in {time.time() - start:.4f} seconds")
            return result
        except Exception as e:
            print(f"Exception in '{func.__name__}': {e}")
            raise
    return wrapper

@logging_decorator
def example_task(x, y):
    time.sleep(1)
    return x + y

if __name__ == "__main__":
    example_task(5, 10)

