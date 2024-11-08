import math


# Naive Approach
def prime_fact(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(log2(n))
    """
    ans = []
    for i in range(2, n+1):
        while n % i == 0:
            ans.append(i)
            n = n // i

    return ans


# Optimized Approach
def prime_fact_op(n):
    """
    Time Complexity: O(sqrt(n))
    Space Complexity: O(log2(n))
    """
    ans = []
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt+1):
        while n % i == 0:
            ans.append(i)
            n = n // i

    if n > 1:
        ans.append(n)

    return ans


print(prime_fact(35))
print(prime_fact_op(35))
