# Problem link: http://projecteuler.net/index.php?section=problems&id=28

res = 0
rightBottomCorner = 1
N = 1001 / 2 + 1
for index in range(0, N): # the index of square rectangle
    sideLength = 2 * index + 1 # the side length of square rectangle
    if index == 0:
        res += rightBottomCorner
    else:
        leftBottomCorner = rightBottomCorner + sideLength - 1
        leftUpCorner = leftBottomCorner + sideLength - 1
        rightUpCorner = leftUpCorner + sideLength - 1
        res += rightBottomCorner + leftBottomCorner + leftUpCorner + rightUpCorner
    perimeter = 4 * (sideLength - 1) # the perimeter of the square rectangle
    rightBottomCorner += perimeter + 2 # the right bottom corner of next square rectangle
print res

