# Problem link: http://projecteuler.net/index.php?section=problems&id=5

# Calculate the greatest common divisor
#    p = 25  q = 15
# -> p = 15  q = 25 % 15 = 10
# -> p = 10  q = 15 % 10 = 5
# -> p = 5   q = 10 % 5  = 0
# -> The answer is 5
def gcd(p, q):
    if p <= 0 or q <= 0:
        return -1
    if p < q:
        k = p
        p = q
        q = k
    while q:
        k = q
        q = p % q
        p = k
    return p

def main():
    res = 1
    for k in range(1, 21):
        res = res * k / gcd(res, k)
    print res

if __name__ == "__main__":
    main()
