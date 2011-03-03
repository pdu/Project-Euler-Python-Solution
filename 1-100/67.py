# Problem link: http://projecteuler.net/index.php?section=problems&id=67

import sys

# read the input
L = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    M = []
    for s in line.split(' '):
        M.append(int(s))
    L.append(M)

# dynamic programming, calculate from bottom to up
for i in range(len(L) - 2, -1, -1):
    for j in range(0, len(L[i])):
        L[i][j] += max(L[i + 1][j], L[i + 1][j + 1])
print L[0][0]

