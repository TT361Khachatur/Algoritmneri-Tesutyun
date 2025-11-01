def kmp_search(text, pat):
    if not pat:
        return list(range(len(text)+1))
    m = len(pat)
    lps = [0]*m
    length = 0
    i = 1
    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    res = []
    i = j = 0
    while i < len(text):
        if text[i] == pat[j]:
            i += 1; j += 1
            if j == m:
                res.append(i-j)
                j = lps[j-1]
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
    return res
