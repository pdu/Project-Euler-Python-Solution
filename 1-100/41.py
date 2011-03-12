# Problem link: http://projecteuler.net/index.php?section=problems&id=41

from myMath import genPrime

primes = []

def isPrime(n):
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

def dfs(kth, n, used, digits):
    if kth == n:
        num = 0
        for i in range(0, n):
            num = num * 10 + digits[i]
        # print num, isPrime(num)
        if isPrime(num):
            return num
        else:
            return 0
    for k in range(n, 0, -1):
        if not used[k]:
            digits[kth] = k
            used[k] = True
            res = dfs(kth + 1, n, used, digits)
            if res != 0:
                return res
            used[k] = False
    return 0

def findPandigitalPrime(n):
    used = [False] * (n + 1)
    digits = [0] * n
    return dfs(0, n, used, digits)

m = 40000
primes = genPrime(m)
n = 9
res = 0
while True:
    res = findPandigitalPrime(n)
    if res != 0:
        break
    n -= 1
print res

