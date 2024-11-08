prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

dp = [[-1 for i in range(2)] for j in range(n)]


def stocks(n, buy):
    if n == len(prices):
        return 0

    if dp[n][buy] != -1:
        return dp[n][buy]

    if buy:
        _buy = stocks(n+1, False) - prices[n]
        not_buy = stocks(n+1, True)
        profit = max(_buy, not_buy)
    else:
        sell = prices[n] + stocks(n+1, True)
        not_sell = stocks(n+1, False)
        profit = max(sell, not_sell)

    dp[n][buy] = profit
    return dp[n][buy]


def stocks2(n):
    dp = [[-1 for i in range(2)] for j in range(n+1)]

    dp[n] = [0, 0]

    for i in range(n-1, -1, -1):
        for j in range(2):
            if j:
                _buy = dp[i+1][0] - prices[i]
                not_buy = dp[i+1][1]
                profit = max(_buy, not_buy)
            else:
                sell = prices[i] + dp[i+1][1]
                not_sell = dp[i+1][0]
                profit = max(sell, not_sell)

            dp[i][j] = profit

    return dp[0][-1]


def stocks3(n):
    next = [0, 0]

    for i in range(n-1, -1, -1):
        for j in range(1, -1, -1):
            if j:
                _buy = next[0] - prices[i]
                not_buy = next[1]
                profit = max(_buy, not_buy)
            else:
                sell = prices[i] + next[1]
                not_sell = next[0]
                profit = max(sell, not_sell)

            next[j] = profit

    return next[-1]


print(stocks(0, True))
print(stocks2(n))
print(stocks3(n))
