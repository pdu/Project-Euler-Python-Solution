# Problem link: http://projecteuler.net/index.php?section=problems&id=46

from myMath import genPrime

n = 10000
primeList = genPrime(n)
primeDict = {}
for prime in primeList:
    primeDict[prime] = True
k = 3
while True:
    if not primeDict.has_key(k):
        can = False
        root = 1
        while True:
            p = k - 2 * root * root
            if p < 0:
                break
            if primeDict.has_key(p):
                can = True
                break
            root += 1
        if not can:
            break
    k += 2
print k

