# Find common elements in 3 sorted arrays

def commonElements (A, B, C, n1, n2, n3):
    i, j, k = 0, 0, 0
    ans = []
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] and B[j] == C[k] and not (A[i] in ans):
            ans.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1

    return ans

A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(commonElements(A, B, C, len(A), len(B), len(C)))