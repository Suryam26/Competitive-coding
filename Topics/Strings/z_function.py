def str_str(haystack: str, needle: str) -> int:
    ans = -1
    n, m = len(haystack), len(needle)

    if m > n:
        return -1

    i, j = 0, 0
    while i < n:
        if haystack[i] == needle[j]:
            k = i
            while j < m and k < n and haystack[k] == needle[j]:
                k += 1
                j += 1

            if j == m:
                ans = k - j
                return ans

            j = 0

        i += 1

    return ans


print(str_str("mississippi", "issip"))
