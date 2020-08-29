# Both decorators keep track of how many times a function is called


# Implemented with functions
import functools

def count(func):
    counter = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        func(*args, **kwargs)
        counter += 1
        print(counter)
    return wrapper
    
    
    
    
# Implemented with classes 
# Source: https://realpython.com/primer-on-python-decorators/#more-real-world-examples
# Section: Classes as Decorators
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
