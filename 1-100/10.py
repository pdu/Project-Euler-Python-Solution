# Problem link: http://projecteuler.net/index.php?section=problems&id=10

from myMath import genPrime

primes = genPrime(2000000)
summ = 0
for k in primes:
    summ += k
print summ

