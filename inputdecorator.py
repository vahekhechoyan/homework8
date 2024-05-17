from functools import wraps

def input_validation_decorator(validation_func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if validation_func(*args, **kwargs):
                return func(*args, **kwargs)
            raise ValueError("Input validation failed")
        return wrapper
    return decorator

@input_validation_decorator
def multiply(x, y):
    return x * y if x >= 0 and y >= 0 else None

if __name__ == "__main__":
    try:
        result = multiply(-1, 5)
    except ValueError as e:
        print(f"Validation error: {e}")
