'''
Problem Statement: https://www.codechef.com/LTIME96B/problems/TANDJ1
Problem Code: TANDJ1
'''


for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())

    dist = abs(c-a) + abs(d-b)

    if dist <= k and (k - dist) % 2 == 0:
        print("YES")
    else:
        print("NO")
