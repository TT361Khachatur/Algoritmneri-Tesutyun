def naive_string_search(text, pat):
    n = len(text); m = len(pat)
    res = []
    for i in range(n-m+1):
        ok = True
        for j in range(m):
            if text[i+j] != pat[j]:
                ok = False
                break
        if ok:
            res.append(i)
    return res
