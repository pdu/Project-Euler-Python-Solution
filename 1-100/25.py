# Problem link: http://projecteuler.net/index.php?section=problems&id=25

def numberOfDigits(N):
    if N == 0:
        return 1
    res = 0
    while N != 0:
        res += 1
        N /= 10
    return res

n = 1000
F1 = 1
F2 = 1
index = 3
while True:
    F3 = F1 + F2
    if numberOfDigits(F3) >= n:
        break
    F1 = F2
    F2 = F3
    index += 1
print index

