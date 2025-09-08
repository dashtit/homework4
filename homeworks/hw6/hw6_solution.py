def level_up(experience: int, threshold: int, reward: int) -> bool:
    return threshold <= experience + reward


def motor_time(n: int) -> int:
    hours = n // 60
    minutes = n % 60
    hours_first = hours // 10
    hours_second = hours % 10
    minutes_first = minutes // 10
    minutes_second = minutes % 10
    return hours_first + hours_second + minutes_first + minutes_second


def time_converter(time_str: str) -> str:
    time_split = time_str.split(':')
    hour = int(time_split[0])
    if hour == 12:
        return ':'.join(time_split) + ' p.m.'
    if hour == 0:
        time_split[0] = '12'
        return ':'.join(time_split) + ' a.m.'
    if hour > 12:
        hour -= 12
        time_split[0] = str(hour)
        return ':'.join(time_split) + ' p.m.'
    else:
        time_split[0] = str(hour)
        return ':'.join(time_split) + ' a.m.'
