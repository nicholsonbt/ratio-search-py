import math

def binarySearch(arr, lower, upper, value):
    if upper < lower:
        return [-1, 1]

    mid = (upper + lower) // 2

    if arr[mid] == value:
        return [mid, 1]

    elif arr[mid] > value:
        val, recs = binarySearch(arr, lower, mid - 1, value)

    else:
        val, recs = binarySearch(arr, mid + 1, upper, value)

    return [val, recs + 1]


def ratioSearch(arr, lower, upper, k, value):
    if upper < lower or k < 0 or k > 1:
        return [-1, 1]

    x = lower + int((upper - lower) * k)

    if arr[x] == value:
        return [x, 1]

    elif arr[x] > value:
        y = arr[x-1] - arr[lower]

        if y <= 0:
            return [-1, 1]
        
        k = (value - arr[lower]) / y
        val, recs = ratioSearch(arr, lower, x - 1, k, value)

    else:
        y = arr[upper] - arr[x + 1]

        if y <= 0:
            return [-1, 1]
        
        k = (value - arr[x + 1]) / y
        val, recs = ratioSearch(arr, x + 1, upper, k, value)

    return [val, recs + 1]
