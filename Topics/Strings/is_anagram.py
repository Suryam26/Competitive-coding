def is_anagram(s: str, t: str) -> bool:
    n, m = len(s), len(t)

    if n != m:
        return False

    dict1, dict2 = {}, {}
    for i in range(n):
        if s[i] not in dict1:
            dict1[s[i]] = 0
        dict1[s[i]] += 1

        if t[i] not in dict2:
            dict2[t[i]] = 0
        dict2[t[i]] += 1

    return dict1 == dict2


def is_anagram2(s: str, t: str) -> bool:
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    return s==t


print(is_anagram("anagram", "nagaram"))
print(is_anagram2("anagram", "nagaram"))
