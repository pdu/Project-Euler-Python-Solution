# Problem link: http://projecteuler.net/index.php?section=problems&id=39

# a = (p * p - 2 * p * b) / (2 * p - 2 * b)
maxCount = 0
res = 0
for p in range(1, 1001):
    count = 0
    for b in range(1, p):
        if (p * p - 2 * p * b) % (2 * p - 2 * b) == 0:
            a = (p * p - 2 * p * b) / (2 * p - 2 * b)
            if a <= b:
                count += 1
    if count > maxCount:
        maxCount = count
        res = p
print res

