from functools import wraps

def caching_decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        return cache[key] if key in cache else cache.setdefault(key, func(*args, **kwargs))

    return wrapper


@caching_decorator
def expensive_operation(x, y):
    return x * y

if __name__ == "__main__":

    print(expensive_operation(2, 3)) 

    
    print(expensive_operation(2, 3))  
