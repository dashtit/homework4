def cache(func):
    already_cached = {}

    def wrapper(*args):
        if args in already_cached:
            return already_cached[args]
        result = func(*args)
        already_cached[args] = result
        return result
    return wrapper


@cache
def cache_function(n: int) -> int:
    if n <= 1:
        return n
    return cache_function(n - 1) + cache_function(n - 2)
