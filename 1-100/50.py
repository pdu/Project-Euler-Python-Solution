# Problem link: http://projecteuler.net/index.php?section=problems&id=50

from myMath import genPrime

n = 1000000
primeList = genPrime(n)
D = {}
for prime in primeList:
    D[prime] = True
num = len(primeList)
summ = [0] * num
for i in range(0, num):
    summ[i] = primeList[i]
    if i != 0:
        summ[i] += summ[i - 1]
resCnt = 0
resValue = 0
for i in range(0, num - resCnt):
    if primeList[i] * resCnt > n:
        break
    for j in range(i + resCnt, num):
        if i == 0:
            value = summ[j]
        else:
            value = summ[j] - summ[i - 1]
        if value >= n:
            break
        cnt = j - i + 1
        if D.has_key(value) and cnt > resCnt:
            resCnt = cnt
            resValue = value
print resCnt, resValue

