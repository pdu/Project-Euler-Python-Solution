# Problem link: http://projecteuler.net/index.php?section=problems&id=9

find = False
for a in range(1, 1001):
    for b in range(a + 1, 1001):
        c = 1000 - a - b
        if c < b:
            break
        if a * a + b * b == c * c:
            find = True
            print a * b * c
            break
    if find:
        break

