from collections.abc import Callable


def typed(type_is):
    def decorator_type(func: Callable) -> Callable:
        def wrapper(*args):
            args_list = []
            for arg in args:
                args_list.append(type_is(arg))
            return func(*args_list)
        return wrapper
    return decorator_type


@typed(type_is=str)
def add_str(*args) -> str:
    return ''.join(args)


@typed(type_is=float)
def add_float(*args) -> float:
    summary = 0
    for arg in args:
        summary += arg
    return summary


@typed(type_is=int)
def add_int(*args) -> int:
    return sum(args)
