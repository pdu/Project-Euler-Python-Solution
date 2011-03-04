# Problem link: http://projecteuler.net/index.php?section=problems&id=20

n = 1
for i in range(1, 101):
    n *= i
res = 0
while n != 0:
    res += n % 10
    n /= 10
print res

