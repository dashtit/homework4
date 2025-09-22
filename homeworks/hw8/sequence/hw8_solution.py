def ascending_sequence(arr: list) -> bool:
    deletion = 0
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            deletion += 1
            if deletion > 1:
                return False
            if i > 0 and arr[i - 1] >= arr[i + 1]:
                return False
    return True
