def exponential_search(arr, target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    lo = i//2
    hi = min(i, n-1)
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
