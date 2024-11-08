# Approach: A prime number has only 2 factors, 1 and the number itself.
import math


# Naive Solution
def check_prime(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return 'Prime'
    return 'Not Prime'


# Optimized Solution
def check_prime_op(n):
    """
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    count = 0
    sqrt = int(math.sqrt(n))
    for i in range(1, sqrt + 1):
        if n % i == 0:
            count += 1
            if i != n / i:
                count += 1

    if count == 2:
        return 'Prime'
    return 'Not Prime'


print(check_prime(17))
print(check_prime_op(17))
