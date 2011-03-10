# Problem link: http://projecteuler.net/index.php?section=problems&id=37

from myMath import genPrime

n = 1000000
primes = genPrime(n)
D = {}
for prime in primes:
    D[prime] = True
res = 0
for prime in primes:
    if prime < 10:
        continue
    ok = True
    mod = 10
    while True:
        if mod > prime:
            break
        if not D.has_key(prime % mod) or not D.has_key(prime / mod):
            ok = False
            break
        mod *= 10
    if ok:
        res += prime
print res

