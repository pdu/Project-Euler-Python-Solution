# Problem link: http://projecteuler.net/index.php?section=problems&id=2

MAX_NUM = 4000000

first = 1
second = 2
sum = 0
while second <= MAX_NUM:
    if second % 2 == 0:
        sum += second
    second += first
    first = second - first
print sum

