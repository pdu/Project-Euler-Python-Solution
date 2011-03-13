# Problem link: http://projecteuler.net/index.php?section=problems&id=48

mod = 10000000000
n = 1000
res = 0
for k in range(1, n + 1):
    res = (res + k ** k) % mod
print res

