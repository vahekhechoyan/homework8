import time
from functools import wraps

def retry_decorator(max_retries=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(delay)
            raise
        return wrapper
    return decorator

@retry_decorator(max_retries=3, delay=2, exceptions=(ValueError,))
def example_task(x, y):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x + y

if __name__ == "__main__":
    try:
        example_task(-1, 10)
    except Exception as e:
        print(f"Task failed with exception: {e}")
