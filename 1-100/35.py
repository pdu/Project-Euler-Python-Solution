# Problem link: http://projecteuler.net/index.php?section=problems&id=35

# use dictionary and prime generator
from myMath import genPrime

def getDigits(n):
    L = []
    while n != 0:
        L.append(n % 10)
        n /= 10
    return L

n = 1000000
L = genPrime(n);
D = {}
for prime in L:
    D[prime] = True
res = 0
for prime in L:
    ok = True
    digits = getDigits(prime)
    num = len(digits)
    for i in range(0, num):
        value = 0
        for j in range(i, i - num, -1):
            value = value * 10 + digits[j]
        if not D.has_key(value):
            ok = False
            break
    if ok:
        res += 1
print res

