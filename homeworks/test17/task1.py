SOME_STRING = 'This is a long long string'


assert SOME_STRING[0] == 'T'
assert SOME_STRING[-1] == 'g'
assert SOME_STRING[2] == 'i'
assert SOME_STRING[-3] == 'i'
assert len(SOME_STRING) == 26
assert SOME_STRING[::-1] == 'gnirts gnol gnol a si sihT'
assert SOME_STRING[0:7] == 'This is'
