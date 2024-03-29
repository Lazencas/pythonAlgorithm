from itertools import *
N, M = map(int,input().split())
a = list(map(str,input().split()))
b = permutations(a,M)
b = list(set(b)).sort()
for i in b:
    print(*i)
