# Problem: Generate all combinations of characters from a string
# up to length k in lexicographical order.


from itertools import combinations

s, k = input().split()

a = sorted(s)
b = int(k)

for i in range(1, b + 1):
    r = combinations(a, i)

    for j in r:
        print("".join(j))
