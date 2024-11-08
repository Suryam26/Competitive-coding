def roman_to_int(s):
    val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    n = len(s)
    ans = 0

    i = 0
    while i < n:
        cha1 = val[s[i]]

        if i+1 < n:
            cha2 = val[s[i+1]]

            if cha1 >= cha2:
                ans += cha1
                i += 1
            else:
                ans += cha2 - cha1
                i += 2

        else:
            ans += cha1
            i += 1

    return ans


print(roman_to_int("MCMIV"))
