# Problem link: http://projecteuler.net/index.php?section=problems&id=29

# use dictionary to keep the distinct terms
D = {}
for a in range(2, 101):
    for b in range(2, 101):
        v = a ** b
        if not v in D:
            D[v] = True
print len(D)

