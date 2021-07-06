'''
Problem Statement: https://www.codechef.com/JULY21C/problems/XXOORR
Problem Code: XXOORR
'''

import math


def decimalToBinary(n):
    binary = str(bin(n).replace("0b", ""))
    return binary[::-1]


def calXOR(n, k, arr):
    for i in range(n):
        arr[i] = decimalToBinary(arr[i])

    count = {}
    for i in arr:
        for j in range(len(i)):
            if i[j] == '1':
                if j not in count:
                    count[j] = 0
                count[j] += 1

    minCount = 0
    for i in count:
        minCount += math.ceil(count[i]/k)

    return minCount


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(calXOR(n, k, arr))
