def add_one(numbers):
    number = int(''.join(map(str, numbers))) + 1
    new_numbers = []
    for number in str(number):
        new_numbers.append(int(number))
    return new_numbers

assert add_one([9]) == [1, 0]
assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([1, 1, 9]) == [1, 2, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
