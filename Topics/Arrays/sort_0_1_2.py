# Dutch National Flag
def sort012(arr, n):
    l, r, m = 0, n-1, 0
    while m <= r:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[r] = arr[r], arr[m]
            r -= 1


a = [0, 1, 2, 2, 1, 0]
sort012(a, len(a))
print(a)
