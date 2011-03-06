# Problem link: http://projecteuler.net/index.php?section=problems&id=27

# Judge whether n is prime or not
def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

maxNum = 0
res_a = 0
res_b = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        # n * n + a * n + b
        n = 0
        while True:
            v = n * n + a * n + b
            if not isPrime(v):
                break
            n += 1
        if n > maxNum:
            maxNum = n
            res_a = a
            res_b = b
print res_a * res_b

