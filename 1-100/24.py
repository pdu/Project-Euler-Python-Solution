# Problem link: http://projecteuler.net/index.php?section=problems&id=24

# Find the N-th permutation in L
# The elements in L is sorted in lexicographic order
# The index of N starts from 0
def findNthPermutation(L, N):
    sz = len(L)
    if sz == 0:
        return []
    # if the first index is decided, the number of permutations
    num = 1
    for i in range(1, sz):
        num *= i
    # Determine the first index, and push back to result
    index = N / num
    res = [L[index]]
    # Find the permutations of the rest, and push back to result
    restCount = N % num
    L.pop(index)
    res += findNthPermutation(L, restCount)
    return res

buf = '0123456789'
n = 999999
print "".join(findNthPermutation(list(buf), n))

