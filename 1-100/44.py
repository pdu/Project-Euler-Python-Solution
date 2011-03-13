# Problem link: http://projecteuler.net/index.php?section=problems&id=44

n = 3000
D = {}
for i in range(1, n):
    v = i * (3 * i - 1) / 2
    D[v] = True
res = 0x7fffffff
for i in range(1, n):
    x = i * (3 * i - 1) / 2
    for j in range(i + 1, n):
        y = j * (3 * j - 1) / 2
        if D.has_key(x + y) and D.has_key(y - x):
            res = min(res, y - x)
print res

