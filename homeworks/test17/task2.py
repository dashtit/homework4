def double_number(n):
    return n*n


assert double_number(1) == 1
assert double_number(2) == 4
assert double_number(11) == 121


def if_even(n):
    if not n % 2 == 0:
        return False
    return True


assert if_even(2) is True
assert if_even(3) is False
assert if_even(100) is True
assert if_even(111) is False
