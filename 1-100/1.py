# Problem link: http://projecteuler.net/index.php?section=problems&id=1

sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum

