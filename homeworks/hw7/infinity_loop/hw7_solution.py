def infinity_loop(left: int, right: int) -> bool:
    while left != right:
        left += 1
        right -= 1
        if left > right:
            return True
        if left == right:
            return False
    else:
        return False
