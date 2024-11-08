def my_atoi(s: str) -> int:
    s = s.strip()
    n = len(s)

    ans = ""
    sign = ""
    for i in range(n):
        if i == 0 and s[i] in ['-', '+']:
            sign = s[i]
        elif s[i].isdigit():
            ans += s[i]
        else:
            break

    if not ans:
        return 0

    ans = int(sign+ans)
    if ans > (2 ** 31) - 1:
        return (2 ** 31) - 1
    if ans < -(2 ** 31):
        return -(2 ** 31)
    return ans


print(my_atoi("     -42"))
