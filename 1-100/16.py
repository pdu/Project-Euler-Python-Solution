# Problem link: http://projecteuler.net/index.php?section=problems&id=16

n = 2 ** 1000
sumDigits = 0
while n != 0:
    sumDigits += n % 10
    n /= 10
print sumDigits

