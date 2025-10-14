def if_paly(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


assert if_paly(121) == True
assert if_paly(-121) == False
assert if_paly(10) == False
assert if_paly(0) == True
assert if_paly(1001) == True
assert if_paly(100) == False
