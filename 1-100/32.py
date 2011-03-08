# Problem link: http://projecteuler.net/index.php?section=problems&id=32

def setDigitFlag(flag, n):
    while n != 0:
        flag[n % 10] += 1
        n /= 10

n = 10000
D = {}
for i in range(1, n):
    left = i + 1
    if i <= 10:
        right = 10000
    elif i <= 100:
        right = 1000
    elif i <= 1000:
        right = 100
    else:
        right = 10
    for j in range(left, right):
        k = i * j
        flag = [0] * 10
        setDigitFlag(flag, i)
        setDigitFlag(flag, j)
        setDigitFlag(flag, k)
        ok = True
        for t in range(0, 10):
            if (t == 0 and flag[t] != 0) or (t != 0 and flag[t] != 1):
                ok = False
                break
        if ok:
            D[k] = True
res = 0
for key in D.keys():
    res += key
print res

