def if_paly(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


assert if_paly(121) is True
assert if_paly(-121) is False
assert if_paly(10) is False
assert if_paly(0) is True
assert if_paly(1001) is True
assert if_paly(100) is False
