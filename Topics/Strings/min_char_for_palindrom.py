def min_chars_for_palindrome(s):
    n = len(s)
    m = n // 2

    ans = n - 1
    center = m
    toggle = True

    while center > 0:
        if toggle:
            i, j = center - 1, center + 1
        else:
            i, j = center - 1, center

        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1

        if i < 0:
            ans = min(ans, n - j)

        if not toggle:
            center -= 1

        toggle = not toggle

    return ans


print(min_chars_for_palindrome("ababb"))
