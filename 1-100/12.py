# Problem link: http://projecteuler.net/index.php?section=problems&id=12

from myMath import genPrime

prime = genPrime(10000)

def divisorNumber(n):
    res = 1
    for p in prime:
        if p * p > n:
            break
        k = 0
        while n % p == 0:
            k = k + 1
            n = n / p
        res = res * (k + 1)
    if n != 1:
        res = res * 2
    return res

res = 0
n = 1
while True:
    res = res + n
    n = n + 1
    if divisorNumber(res) >= 500:
        break
print res

