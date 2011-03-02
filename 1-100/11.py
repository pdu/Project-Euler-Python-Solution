# Problem link: http://projecteuler.net/index.php?section=problems&id=11

def str2int(s):
    res = 0
    for c in s:
        res = res * 10 + int(c) - int('0')
    return res

L = []
for i in range(0, 20):
    M = []
    s = raw_input()
    for s1 in s.split(' '):
        M.append(str2int(s1))
    L.append(M)

dir = [[1, 0], [1, 1], [0, 1], [-1, 1]]

product = 0
for i in range(0, 20):
    for j in range(0, 20):
        for k in range(0, 4):
            ii = i + 3 * dir[k][0]
            jj = j + 3 * dir[k][1]
            if ii >= 0 and ii < 20 and jj >= 0 and jj < 20:
                temp = 1
                for t in range(0, 4):
                    temp = temp * L[i + t * dir[k][0]][j + t * dir[k][1]]
                product = max(product, temp)
print product

