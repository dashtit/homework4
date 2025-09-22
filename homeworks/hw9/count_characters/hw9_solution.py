def count_char(raw_str: str) -> str:
    count = 1
    new_str = ''
    for i in range(1, len(raw_str)):
        if raw_str[i] == raw_str[i - 1]:
            count += 1
        else:
            if count > 1:
                new_str += raw_str[i - 1] + str(count)
                count = 1
            else:
                new_str += raw_str[i - 1]
    if count > 1:
        new_str += raw_str[-1] + str(count)
    else:
        new_str += raw_str[-1]
    return new_str
