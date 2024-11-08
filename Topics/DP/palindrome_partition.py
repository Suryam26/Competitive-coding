s = "aab"
n = len(s)


def isPalindrome(string):
    i, j = 0, len(string)-1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False

    return True


dp = [-1 for i in range(n)]


def palindromePartition(i, n):
    if i == n:
        return 0

    if dp[i] != -1:
        return dp[i]

    mini = float('inf')
    for j in range(i, n):
        if isPalindrome(s[i:j+1]):
            cost = 1 + palindromePartition(j+1, n)
            mini = min(mini, cost)

    dp[i] = mini
    return dp[i]


def palindromePartition2(n):
    dp = [-1 for i in range(n+1)]
    dp[n] = 0

    for i in range(n-1, -1, -1):
        mini = float('inf')
        for j in range(i, n):
            if isPalindrome(s[i:j+1]):
                cost = 1 + dp[j+1]
                mini = min(mini, cost)
                dp[i] = mini

    return dp[0]


print(palindromePartition(0, n)-1)
print(palindromePartition2(n)-1)
