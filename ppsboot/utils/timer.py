import time


def timed(func):
    """ Used as a decorator to time a function.

    Example:

    ```python
    @timed
    def my_function():
        ...
    ```

    prints: `my_function took 0.00ms. Result: ...`
    """
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f" {func.__name__} took {(time.time() - start)*1000:.2f}ms. Result: {result}")
        return result
    return inner
