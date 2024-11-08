def allocation_possible(mid, arr, k, n):
    student, pages = 1, 0
    for i in range(n):
        if pages + arr[i] > mid:
            student += 1
            pages = arr[i]
        if arr[i] > mid:
            return False
        else:
            pages += arr[i]

    if student > k:
        return False

    return True


def books(arr, k):
    n = len(arr)
    if k > n:
        return -1

    low = min(arr)
    high = sum(arr)

    while low <= high:
        mid = (low + high) // 2

        if allocation_possible(mid, arr, k, n):
            high = mid - 1
        else:
            low = mid + 1

    return low


A = [12, 34, 67, 90]
B = 2
print(books(A, B))
