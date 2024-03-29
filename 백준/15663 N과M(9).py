from itertools import *
N, M = map(int,input().split())
a = list(map(int,input().split()))
b = permutations(a,M)
b = sorted(list(set(b)))
for i in b:
    print(*i)
