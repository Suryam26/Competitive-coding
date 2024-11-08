import math

from sieve import create_sieve

sieve = create_sieve(1000000)


def generate_primes(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    prime = []
    for i in range(2, n):
        if sieve[i]:
            prime.append(i)

    return prime


def segmented_sieve(l, r):
    prime = generate_primes(int(math.sqrt(r)) + 1)
    seg_sieve = [True] * (r - l + 1)

    for i in prime:
        first_multiple = (l // i) * i
        if first_multiple < l:
            first_multiple += i

        for j in range(max(first_multiple, i * i), r+1, i):
            seg_sieve[j - l] = False

    prime_in_range = []
    for i in range(l, r+1):
        if seg_sieve[i - l]:
            prime_in_range.append(i)

    return prime_in_range


print(segmented_sieve(10, 130))
