def number_opposite(n: int, f_number: int) -> int:
    if f_number < n // 2:
        return f_number + n // 2
    else:
        return (f_number + n // 2) % n
