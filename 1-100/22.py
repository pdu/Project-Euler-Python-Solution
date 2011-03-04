# Problem link: http://projecteuler.net/index.php?section=problems&id=22

import sys

L = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    for s in line.split(','):
        L.append(s[1:-1])
L.sort()

score = 0
index = 0
for s in L:
    index += 1
    value = 0
    for c in s:
        value += ord(c) - ord('A') + 1
    score += value * index
print score

