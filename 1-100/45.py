# Problem link: http://projecteuler.net/index.php?section=problems&id=45

def isPentagonal(t):
    left = 1
    right = 0x7fffffff
    while left <= right:
        mid = (left + right) / 2
        value = mid * (3 * mid - 1) / 2
        if value > t:
            right = mid - 1
        elif value < t:
            left = mid + 1
        else:
            return True
    return False

def isHexagonal(t):
    left = 1
    right = 0x7fffffff
    while left <= right:
        mid = (left + right) / 2
        value = mid * (2 * mid - 1)
        if value > t:
            right = mid - 1
        elif value < t:
            left = mid + 1
        else:
            return True
    return False

res = 0
k = 286
while True:
    t = k * (k + 1) / 2
    if isPentagonal(t) and isHexagonal(t):
        res = t
        break
    k += 1
print res

