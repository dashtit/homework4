def summary_all(n):
    summary = 0
    for i in range(1, n+1):
        summary += i
    return summary


assert summary_all(1) == 1
assert summary_all(2) == 3
assert summary_all(8) == 36
assert summary_all(22) == 253
assert summary_all(100) == 5050
