# Problem link: http://projecteuler.net/index.php?section=problems&id=33

from myMath import gcd

numerator = 1
denominator = 1
for i in range(10, 100):
    iTen = i / 10
    iUnit = i % 10
    for j in range(i + 1, 100):
        jTen = j / 10
        jUnit = j % 10
        ok = False
        if iTen == jTen and i * jUnit == j * iUnit:
            ok = True
        if iTen == jUnit and i * jTen == j * iUnit:
            ok = True
        if iUnit == jTen and i * jUnit == j * iTen:
            ok = True
        # This case considered to be trivial, so ignore it
        # if iUnit == jUnit and i * jTen == j * iTen:
        #     ok = True
        if ok:
            numerator *= i
            denominator *= j
print denominator / gcd(numerator, denominator)

