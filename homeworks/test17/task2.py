def double_number(n):
    return n*n


assert double_number(1) == 1
assert double_number(2) == 4
assert double_number(11) == 121


def if_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


assert if_even(2) == True
assert if_even(3) == False
assert if_even(100) == True
assert if_even(111) == False
