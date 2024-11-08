spf = []


def create_spf_sieve(n):
    """
    Time Complexity: O(n*log(log(n)))
    Space Complexity: O(n)
    """
    global spf
    spf = [i for i in range(n+1)]

    i = 2
    while i*i <= n:
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i

        i += 1


def prime_fact(n):
    """
    Time Complexity: O(log(n))
    Space Complexity: O(log2(n))
    """
    create_spf_sieve(n)
    ans = []
    while n != 1:
        ans.append(spf[n])
        n = n // spf[n]

    return ans


print(prime_fact(21))
