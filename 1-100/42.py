# Problem link: http://projecteuler.net/index.php?section=problems&id=42

import sys

n = 100
D = {}
for k in range(1, n):
    D[ k * (k + 1) / 2] = True
res = 0
while True:
    line = sys.stdin.readline()
    if not line:
        break
    for token in line.split(','):
        word = token[1: -1]
        value = 0
        for c in word:
            value += ord(c) - ord('A') + 1
        if D.has_key(value):
            res += 1
print res

