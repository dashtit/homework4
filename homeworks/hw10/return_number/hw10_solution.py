from collections.abc import Callable


def summary_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            raise ValueError('Arguments should be a number')
        return result
    return wrapper


@summary_decorator
def concat_str(*args, **kwargs) -> str:
    return "".join(list(args) + list(kwargs.values()))


@summary_decorator
def arguments_summary(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())
