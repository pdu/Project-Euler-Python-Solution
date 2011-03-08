# Problem link: http://projecteuler.net/index.php?section=problems&id=34

n = 10000000
factorial = [1] * 10
for i in range(1, 10):
    factorial[i] = factorial[i - 1] * i
res = 0
for i in range(10, n):
    temp = 0
    j = i
    while j != 0:
        temp += factorial[j % 10]
        j /= 10
    if temp == i:
        res += i
print res

