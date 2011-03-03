# Problem link: http://projecteuler.net/index.php?section=problems&id=15

# Dynamic programming
N = 21
L = [[0] * N] * N
for r in range(0, N):
    for c in range(0, N):
        if r == 0 or c == 0:
            L[r][c] = 1
        else:
            L[r][c] = L[r - 1][c] + L[r][c - 1]
print L[N - 1][N - 1]

