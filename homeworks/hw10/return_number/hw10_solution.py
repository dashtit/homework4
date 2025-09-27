def summary_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result
        else:
            raise ValueError('Arguments should be a number')
    return wrapper


@summary_decorator
def concat_str(*args, **kwargs) -> str:
    return "".join(list(args) + list(kwargs.values()))


@summary_decorator
def arguments_summary(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())
