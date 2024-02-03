from itertools import permutations
def perm(a):
    all_per=permutations(a)
    return list(all_per)
a=input()
print(perm(a))