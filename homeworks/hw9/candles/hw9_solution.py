def count_candles(candles: int, leftover: int) -> int:
    got_leftover = 0
    got_candles = candles
    while candles:
        candles -= 1
        got_leftover += 1
        if got_leftover == leftover:
            candles += 1
            got_candles += 1
            got_leftover = 0
    return got_candles
