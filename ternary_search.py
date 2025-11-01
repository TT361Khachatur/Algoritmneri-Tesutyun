def ternary_search(arr, target):
    lo = 0
    hi = len(arr)-1
    while lo <= hi:
        third = (hi - lo) // 3
        m1 = lo + third
        m2 = hi - third
        if arr[m1] == target:
            return m1
        if arr[m2] == target:
            return m2
        if target < arr[m1]:
            hi = m1 - 1
        elif target > arr[m2]:
            lo = m2 + 1
        else:
            lo = m1 + 1
            hi = m2 - 1
    return -1
