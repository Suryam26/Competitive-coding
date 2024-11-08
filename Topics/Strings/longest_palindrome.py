def expand_around_center(s, l, r, n):
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return [r - l - 1, l + 1, r - 1]


def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 1:
        return ""

    max_len, start, end = 0, 0, 0
    for i in range(n):
        len1 = expand_around_center(s, i, i, n)
        len2 = expand_around_center(s, i, i + 1, n)

        if len1[0] > len2[0]:
            max_arr = len1
        else:
            max_arr = len2

        if max_len < max_arr[0]:
            max_len = max_arr[0]
            start = max_arr[1]
            end = max_arr[2]

    return s[start: end + 1]
