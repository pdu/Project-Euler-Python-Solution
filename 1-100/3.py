# Problem link: http://projecteuler.net/index.php?section=problems&id=3

N = 600851475143

res = 0
k = 2
while k * k <= N:
    if N % k == 0:
        res = max(res, k)
        while N % k == 0:
            N /= k
    k += 1
if N != 1:
    res = max(res, N)
print res

