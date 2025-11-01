def boyer_moore_search(text, pat):
    n = len(text); m = len(pat)
    if m == 0:
        return list(range(n+1))
    bad = {}
    for i, ch in enumerate(pat):
        bad[ch] = i
    res = []
    i = 0
    while i <= n-m:
        j = m-1
        while j >= 0 and pat[j] == text[i+j]:
            j -= 1
        if j < 0:
            res.append(i)
            i += 1
        else:
            lo = bad.get(text[i+j], -1)
            shift = max(1, j - lo)
            i += shift
    return res
