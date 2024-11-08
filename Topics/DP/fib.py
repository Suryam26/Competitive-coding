# Memoization
dp = [-1] * 10


def fib1(n):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    return fib1(n-1) + fib1(n-2)


# Tabulation
def fib2(n):
    dp2 = [-1] * (n+1)
    dp2[0], dp2[1] = 0, 1

    for i in range(2, n+1):
        dp2[i] = dp2[i-1] + dp2[i-2]

    return dp2[n]


# Optimized Tabulation
def fib3(n):
    if n <= 1:
        return n

    ans = 0
    prev2, prev = 0, 1
    for i in range(2, n+1):
        ans = prev + prev2
        prev2 = prev
        prev = ans

    return ans


print(fib1(5))
print(fib2(5))
print(fib3(5))
