some_string='This is a long long string'


assert some_string[0] == 'T'
assert some_string[-1] == 'g'
assert some_string[2] == 'i'
assert some_string[-3] == 'i'
assert len(some_string) == 26
assert some_string[::-1] == 'gnirts gnol gnol a si sihT'
assert some_string[0:7] == 'This is'
