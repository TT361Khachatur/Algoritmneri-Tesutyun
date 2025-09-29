def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            matches.append(i)  
    return matches

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        return lps

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    matches = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


def boyer_moore(text, pattern):
    def last_occurrence(pattern):
        L = {}
        for i in range(len(pattern)):
            L[pattern[i]] = i
        return L

    n, m = len(text), len(pattern)
    L = last_occurrence(pattern)
    matches = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            if pattern[j] != text[i + j]:
                lo = L.get(text[i + j], -1)
                i += max(1, j - lo)
                break
            j -= 1
        if j < 0:
            matches.append(i)
            i += 1
    return matches


T1 = "abacaabaccabacabaabb"
P1 = "abacab"

print(kmp_search(T1, P1))
print(boyer_moore(T1, P1))
print(naive_search(T1, P1)) 