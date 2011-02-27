# Problem link: http://projecteuler.net/index.php?section=problems&id=7

def genPrime(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if not isPrime[i]:
            continue
        for j in range(i * i, n + 1, i):
            isPrime[j] = False
    res = []
    for i in range(0, n + 1):
        if isPrime[i]:
            res.append(i)
    return res

def main():
    maxNum = 200000
    primeIndex = 10001
    primeList = genPrime(maxNum)
    if len(primeList) >= primeIndex:
        print primeList[primeIndex - 1]
    else:
        print "Enlarge maxNum\n"

if __name__ == "__main__":
    main()

