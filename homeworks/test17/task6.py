def file_info(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_lines = len(lines)
    num_words = 0
    for line in lines:
        num_words += len(line.split())
    num_letters = 0
    for line in lines:
        for word in line.split():
            num_letters += len(word)
    result = f'String count: {num_lines}\nWord count: {num_words}\nLetter count: {num_letters}\n'
    with open(filename, 'a') as file:
        file.write(result)
    print(result)


file_info('C:\\Homework\\homework4\\homeworks\\test17\\task6.txt')
