# Problem link: http://projecteuler.net/index.php?section=problems&id=43

primes = [2, 3, 5, 7, 11, 13, 17]

def isDivisible(digits, n):
    ok = True
    for i in range(0, 7):
        value = digits[i + 1] * 100 + digits[i + 2] * 10 + digits[i + 3]
        if value % primes[i] != 0:
            ok = False
            break
    return ok

def dfs(kth, n, used, digits):
    if kth == n:
        if isDivisible(digits, n):
            value = 0
            for i in range(0, n):
                value = value * 10 + digits[i]
            return value
        else:
            return 0
    res = 0
    for i in range(0, n):
        if kth == 0 and i == 0:
            continue
        if not used[i]:
            used[i] = True
            digits[kth] = i
            res += dfs(kth + 1, n, used, digits)
            used[i] = False
    return res

n = 10
used = [False] * n
digits = [-1] * n
res = dfs(0, n, used, digits)
print res

