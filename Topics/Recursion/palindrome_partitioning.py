def partition(s):
    n = len(s)

    def is_palindrome(string):
        return string == string[::-1]

    ans = []
    curr = []

    def sol(i):
        if i == n:
            ans.append(curr[:])
            return

        for idx in range(i, n):
            temp = s[i: idx + 1]
            if is_palindrome(temp):
                curr.append(temp)
                sol(idx + 1)
                curr.pop()

    sol(0)
    return ans
