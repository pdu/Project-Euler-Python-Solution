# Problem link: http://projecteuler.net/index.php?section=problems&id=40

def getDigits(n):
    L = []
    while n != 0:
        L.append(n % 10)
        n /= 10
    L.reverse()
    return L

n = 1000000
d = []
k = 1
while True:
    t = getDigits(k)
    d += t
    if len(d) >= n:
        break
    k += 1
res = d[0] * d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999]
print res

