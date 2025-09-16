import random


def generate_secret_number() -> str:
    secret_value = ''
    while len(secret_value) < 4:
        secret_number = str(random.randint(1, 9))
        if secret_value.find(secret_number) == -1:
            secret_value += secret_number
        else:
            continue
    return secret_value


def check_guess(bulls: str, cows: str) -> tuple:
    full_match = 0
    match = 0
    for bull in bulls:
        for cow in cows:
            if bull == cow and bulls.index(bull) == cows.index(bull):
                full_match += 1
            elif bull == cow and bulls.index(bull) != cows.index(bull):
                match += 1
    bulls_and_cows = (full_match, match)
    return bulls_and_cows
