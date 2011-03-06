# Problem link: http://projecteuler.net/index.php?section=problems&id=30

# The number can only have 6 digits
res = 0
for k in range(2, 1000000):
    t = k
    temp = 0
    while t != 0:
        temp += (t % 10) ** 5
        t /= 10
    if temp == k:
        res += k
print res

