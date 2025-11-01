def interpolation_search(arr, target):
    lo = 0
    hi = len(arr)-1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[hi] == arr[lo]:
            if arr[lo] == target:
                return lo
            else:
                return -1
        pos = lo + int((target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]))
        if pos < lo or pos > hi:
            return -1
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1
