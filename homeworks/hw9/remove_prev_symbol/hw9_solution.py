def remove_previous_symbol(raw_str: str) -> str:
    if raw_str == '':
        return raw_str
    split_str = []
    for i, symb in enumerate(raw_str):
        if symb != '#':
            split_str.append(symb)
        if i < len(raw_str) - 1 and raw_str[i + 1] == '#':
            if split_str:
                split_str.pop()
    return ''.join(split_str)
