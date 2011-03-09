# Problem link: http://projecteuler.net/index.php?section=problems&id=36

def getDigits(n, radix):
    L = []
    while n != 0:
        L.append(n % radix)
        n /= radix
    return L

def isPalindromic(n, radix):
    digits = getDigits(n, radix)
    num = len(digits)
    left = 0
    right = num - 1
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    return True

n = 1000000
res = 0
for i in range(1, n):
    if isPalindromic(i, 10) and isPalindromic(i, 2):
        res += i
print res

