# Best Time to Buy and Sell Stock

def maxProfit(prices):
    maxProfit = 0
    minimum = prices[0]
    for i in prices:
        profit = i - minimum
        if  profit < 0:
            minimum = i

        maxProfit = max(maxProfit, profit)

    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
