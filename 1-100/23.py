# Problem link: http://projecteuler.net/index.php?section=problems&id=23

N = 28124
isAbundant = [False] * N
listAbundant = []
for i in range(2, N):
    sumOfProperDivisor = 1
    j = 2
    while j * j <= i:
        if j * j == i:
            sumOfProperDivisor += j
        elif i % j == 0:
            sumOfProperDivisor += j + i / j;
        j += 1
    if sumOfProperDivisor > i:
        isAbundant[i] = True
        listAbundant.append(i)
res = 0
for i in range(1, N):
    flag = False
    for j in listAbundant:
        if j + j > i:
            break
        if isAbundant[i - j]:
            flag = True
            break
    if not flag:
        res += i
print res

