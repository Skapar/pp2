from itertools import permutations
# 5 th task
def perma(s):
    k = [''.join(p) for p in permutations(s)]
    return k

# b=str(input())
# print(perma(b))

# --------------------------------------------