# Problem link: http://projecteuler.net/index.php?section=problems&id=17

# one two three four five six seven eight nine
sum1To9 = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
# ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
sum10To19 = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
# twenty thirty forty fifty sixty seventy eighty ninety
sum20To99 = sum1To9 * 8 + (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) * 10
sum1To99 = sum1To9 + sum10To19 + sum20To99
# x hundred, x hundred and y
sum100To999 = sum1To9 * 100 + 7 * 900 + 3 * 891 + sum1To99 * 9
# one thousand
sum1To1000 = sum1To99 + sum100To999 + 3 + 8
print sum1To1000

