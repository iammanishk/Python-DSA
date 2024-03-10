# ---------------------------------------------------- DECORATORS ----------------------------------------------------
import time

# Write a decorator that measures the time a function takes to execute:

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)


example_function(5)


# Create a decorator to print the functioin name and the value of its arguments every time a function is called:


def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwarg_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling {func.__name__} with args {arg_value} and kwargs {kwarg_value}")
        return func(*args, **kwargs)
    
    return wrapper

@debug
def greet(name, greeting="Hello "):
    print(f"{greeting}{name}")

greet("Manish")

greet("Anubhav", "How are you")


# Impliment a decorator that caches the return value of a function, so that when it called with the same arguments, the cached value is returned insted of calling the function again:


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        return result
    return wrapper





@cache
def long_running_function(a, b):
    time.sleep(5)
    sum = a + b
    return sum


print(long_running_function(1, 2))
print(long_running_function(1, 2))