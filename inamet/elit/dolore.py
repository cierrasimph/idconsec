def time_spent(func):
    """Decorator that prints the time spent in executing a function.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time spent in {func.__name__}: {end - start:.6f} seconds")
        return result

    return wrapper
