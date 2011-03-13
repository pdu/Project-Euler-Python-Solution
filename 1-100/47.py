# Problem link: http://projecteuler.net/index.php?section=problems&id=47

from myMath import genPrime

n = 100000
primes = genPrime(n)

def getPrimeFactorNum(k):
    cnt = 0
    for prime in primes:
        if prime * prime > k:
            break
        if k % prime == 0:
            cnt += 1
            while k % prime == 0:
                k /= prime
    if k != 1:
        cnt += 1
    return cnt

factorNum = [0] * 4
factorNum[0] = getPrimeFactorNum(1)
factorNum[1] = getPrimeFactorNum(2)
factorNum[2] = getPrimeFactorNum(3)
factorNum[3] = getPrimeFactorNum(4)
k = 5
res = 0
while True:
    id = (k - 1) % 4
    factorNum[id] = getPrimeFactorNum(k)
    ok = True
    for i in range(0, 4):
        if factorNum[i] != 4:
            ok = False
            break
    if ok:
        res = k - 3
        break
    k += 1
print res

