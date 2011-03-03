# Problem link: http://projecteuler.net/index.php?section=problems&id=14

def getChainNumber(k, L):
    if k < len(L) and L[k] != 0:
        return L[k]
    if k == 1:
        L[1] = 1
        return 1
    if k % 2 == 0:
        next = 1 + getChainNumber(k / 2, L)
        if k < len(L):
            L[k] = next
        return next
    else:
        next = 1 + getChainNumber(3 * k + 1, L)
        if k < len(L):
            L[k] = next
        return next

N = 1000000
L = [0] * N
res = 0
maxChainNumber = 0
for k in range(1, N):
    L[k] = getChainNumber(k, L)
    if L[k] > maxChainNumber:
        maxChainNumber = L[k]
        res = k
print res

