'''
Problem Statement: https://www.codechef.com/START6C/problems/JOKRBTMN
Problem Code: JOKRBTMN
'''


def calSegments(n, m, l, arr, strip):
    count = {}
    for i in range(m):
        for j in range(1, arr[i][0]+1):
            count[arr[i][j]] = i+1

    segment = 1
    for i in range(l-1):
        if count[strip[i]] != count[strip[i+1]]:
            segment += 1

    return segment


for _ in range(int(input())):
    n, m, l = map(int, input().split())
    arr = []
    for i in range(m):
        tempList = list(map(int, input().split()))
        arr.append(tempList)
    strip = list(map(int, input().split()))

    print(calSegments(n, m, l, arr, strip))
