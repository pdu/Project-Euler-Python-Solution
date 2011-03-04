# Problem link: http://projecteuler.net/index.php?section=problems&id=21

N = 10001
L = [0] * (3 * N)
for i in range(2, 3 * N):
    L[i] = 1
    j = 2
    while j * j <= i:
        if j * j == i:
            L[i] += j
        elif i % j == 0:
            L[i] += j + i / j
        j += 1
res = 0
for i in range(1, N):
    j = L[i]
    if i != j and L[j] == i:
        res += i
print res

