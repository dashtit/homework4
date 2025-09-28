from collections.abc import Callable


def validate_arguments(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        arguments = list(args) + list(kwargs.values())
        for arg in arguments:
            if arg <= 0:
                raise ValueError(f'{arg} is not a positive')
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def sum_positive(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())
