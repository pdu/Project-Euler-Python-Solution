# Problem link: http://projecteuler.net/index.php?section=problems&id=31

# dynamic programming
coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200
ways = [0] * (n + 1)
ways[0] = 1
for coin in coins:
    for total in range(coin, n + 1):
        ways[total] += ways[total - coin]
print ways[n]

