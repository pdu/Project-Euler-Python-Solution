# Problem link: http://projecteuler.net/index.php?section=problems&id=38

def getDigits(n):
    L = []
    while n != 0:
        L.append(n % 10)
        n /= 10
    L.reverse()
    return L

n = 10000
res = 123456789
for i in range(1, n):
    digits = [0] * 10
    j = 1
    temp = 0
    while True:
        k = i * j
        d = getDigits(k)
        for t in d:
            temp = temp * 10 + t
            digits[t] += 1
        brk = False
        digitSum = 0
        for t in range(0, 10):
            digitSum += digits[t]
            if (t == 0 and digits[t] > 0) or (t != 0 and digits[t] > 1):
                brk = True
                break
        if brk:
            break
        if digitSum == 9:
            res = max(res, temp)
            break
        j += 1
print res

