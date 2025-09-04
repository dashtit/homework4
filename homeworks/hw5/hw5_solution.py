def add_ing(s: str) -> str:
    s += 'ing'
    return s


def change_symbol(s: str) -> str:
    s = s.replace('#', '/')
    return s


def change_order(s: str) -> str:
    new_list = s.split()
    new_list.reverse()
    return ' '.join(new_list)


def clean_string(s: str) -> str:
    s = s.strip()
    return s


def to_capitalize(s: str) -> str:
    s = s.capitalize()
    return s


def to_list(s: str) -> list:
    new_list = s.split()
    return new_list


def formatting(array: list, s1: str, s2: str) -> str:
    new_str = ' '.join(array)
    return f"Hello, {new_str}! {s1} to {s2}"


def to_string(array: list) -> str:
    new_str = ' '.join(array)
    return new_str


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array.insert(indx, item)
    return array


def delete_from_list(array: list, indx: int) -> list:
    del array[indx]
    return array
