'''
Problem Statement: https://www.codechef.com/START6C/problems/ETUP
Problem Code: ETUP
'''


def NC3(x):
    if x < 3:
        return 0
    elif x == 3:
        return 1
    else:
        return (x*(x-1)*(x-2))//6


def NC2(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    else:
        return (x*(x-1))//2


for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    even = [0]
    for i in range(n):
        if arr[i] % 2 == 0:
            even.append(even[i]+1)
        else:
            even.append(even[i])

    for i in range(q):
        q1, q2 = map(int, input().split())
        e = even[q2] - even[q1-1]
        o = (q2-q1+1) - e
        print(NC3(e) + (NC2(o)*e))
