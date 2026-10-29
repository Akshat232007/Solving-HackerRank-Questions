# Problem: Generate all permutations of length k
# from the given string in lexicographical order.

from itertools import permutations

s , k = input().split()
a = sorted(s)
b = int(k)
p = permutations(a,b)

for i in p:
    print("".join(i))
