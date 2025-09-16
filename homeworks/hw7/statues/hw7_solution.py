def missing_statues(arr: list) -> int:
    if arr:
        max_value = max(arr)
        min_value = min(arr)
        new_arr = range(min_value, max_value + 1)
        unique_values = set(arr) ^ set(new_arr)
        return len(unique_values)
    else:
        return 0
