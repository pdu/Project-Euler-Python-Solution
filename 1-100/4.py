# Problem link: http://projecteuler.net/index.php?section=problems&id=4

def isPalindrome(n):
    if n < 0:
        return False
    digits = []
    while n:
        digits.append(n % 10)
        n = n / 10
    i = 0
    j = len(digits) - 1
    while i < j:
        if digits[i] != digits[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def main():
    res = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            if isPalindrome(k):
                res = max(res, k);
    print res

if __name__ == "__main__":
    main()