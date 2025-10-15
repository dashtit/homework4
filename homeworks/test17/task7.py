def string_remaster(some_str, num):
    if num == 1:
        return some_str[:1]
    return some_str[:num] + some_str[num-2::-1]


assert string_remaster('abcdefghijklmnopqrstuvwxyz', 1) == 'a'
assert string_remaster('abcdefghijklmnopqrstuvwxyz', 2) == 'aba'
assert string_remaster('abcdefghijklmnopqrstuvwxyz', 3) == 'abcba'
assert string_remaster('abcdefghijklmnopqrstuvwxyz', 4) == 'abcdcba'
