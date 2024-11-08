def n_queens(n):
    ans = []

    def is_safe(r, c, board):
        for i in range(n):
            if board[i][c] == 'Q':
                return False
            if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 'Q':
                return False
            if r - i >= 0 and c + i < n and board[r - i][c + i] == 'Q':
                return False
        return True

    arr = ['.' * n for i in range(n)]

    def sol(r):
        if r == n:
            ans.append(arr[:])
            return

        for c in range(n):
            if is_safe(r, c, arr):
                temp = list(arr[r])
                temp[c] = 'Q'
                arr[r] = ''.join(temp)

                sol(r + 1)

                temp[c] = '.'
                arr[r] = ''.join(temp)

    sol(0)
    return ans
