# Problem link: http://projecteuler.net/index.php?section=problems&id=6

sumOfSquares = 0
summ = 0
for k in range(1, 101):
    sumOfSquares += k * k
    summ += k
squareOfSum = summ * summ
print squareOfSum - sumOfSquares

