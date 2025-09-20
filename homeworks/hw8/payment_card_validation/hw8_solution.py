def is_card_number_valid(number) -> bool:
    flag = False
    summary = 0
    if isinstance(number, int):
        card = str(number)[::-1]
        card_first = card[1::2]
        card_second = card[::2]
        for i in card_first:
            if int(i) * 2 <= 9:
                summary += int(i) * 2
            else:
                summary += int(i) * 2 - 9
        for i in card_second:
            summary += int(i)
        if summary % 10 == 0:
            flag = True
    return flag
