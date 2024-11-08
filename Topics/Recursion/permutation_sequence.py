def get_permutation(n, k):
    ans = []

    def sol(s):
        nonlocal k
        if k == 0:
            return

        if len(s) == n:
            ans.append(s)
            k -= 1
            return

        for j in range(1, n + 1):
            if str(j) not in s:
                sol(s + str(j))

    sol("")
    return ans[-1]
