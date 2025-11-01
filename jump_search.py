def jump_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    step = int(n**0.5)
    prev = 0
    while prev < n and arr[min(n-1, prev+step-1)] < target:
        prev += step
        if prev >= n:
            return -1
    for i in range(prev, min(prev+step, n)):
        if arr[i] == target:
            return i
    return -1
