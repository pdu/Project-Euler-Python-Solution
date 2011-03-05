# Problem link: http://projecteuler.net/index.php?section=problems&id=26

# return length of recurring cycle: m / n
# judge the recurring cycle by remainder
def findRecurringCycleLength(m, n):
    m = m % n
    L = [-1] * n
    L[m] = 0
    res = 0
    index = 1
    while m != 0:
        m = (m * 10) % n
        if L[m] == -1:
            L[m] = index
        else:
            res = index - L[m]
            break
        index += 1
    return res

res = 0
maxLength = 0
for d in range(1, 1000):
    length = findRecurringCycleLength(1, d)
    if length > maxLength:
        maxLength = length
        res = d
print res

