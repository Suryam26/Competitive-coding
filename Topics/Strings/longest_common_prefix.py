def longest_common_prefix(strs: list[str]) -> str:
    ans = strs[0]

    for word in strs:
        temp = ans
        n = len(temp)
        m = len(word)

        i, j = 0, 0
        ans = ""
        while i < n and j < m:
            if temp[i] == word[j]:
                ans += word[j]
                i += 1
                j += 1
            else:
                break

    return ans


print(longest_common_prefix(["flower", "flow", "flight"]))
