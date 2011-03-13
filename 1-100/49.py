# Problem link: http://projecteuler.net/index.php?section=problems&id=49

from myMath import genPrime

def getDigits(n):
    res = []
    while n != 0:
        res.append(n % 10)
        n /= 10
    return res

def haveSameDigits(n, m):
    a = getDigits(n)
    b = getDigits(m)
    a.sort()
    b.sort()
    if len(a) != len(b):
        return False
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True

n = 10000
primes = genPrime(n)
D = {}
for prime in primes:
    D[prime] = True
num = len(primes)
for i in range(0, num):
    if primes[i] <= 1000:
        continue
    for j in range(i + 1, num):
        k = 2 * primes[j] - primes[i]
        if not D.has_key(k):
            continue
        if haveSameDigits(primes[i], primes[j]) and haveSameDigits(primes[i], k):
            print "%d%d%d" % (primes[i], primes[j], k)

