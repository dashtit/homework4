def ascending_sequence(arr: list) -> bool:
    deletion = 0
    flag = True
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1] and deletion >= 1:
            flag = False
        if arr[i] >= arr[i + 1] and deletion < 1:
            deletion += 1
        if i > 0 and arr[i - 1] >= arr[i + 1]:
            flag = False
    return flag
