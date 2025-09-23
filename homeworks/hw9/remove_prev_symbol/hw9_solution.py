def remove_previous_symbol(raw_str: str) -> str:
    if raw_str == '':
        return raw_str
    split_str = []
    for _, symb in enumerate(raw_str):
        if symb != '#':
            split_str.append(symb)
        else:
            if split_str:
                split_str.pop()
    return ''.join(split_str)
