def create_sieve(n):
    """
    Time Complexity: O(n*log(log(n)))
    Space Complexity: O(n)
    """
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False

    i = 2
    while i*i <= n:
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

        i += 1

    return sieve


prime = create_sieve(25)
print(prime[4])
