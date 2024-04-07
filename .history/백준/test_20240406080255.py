from heapq import *

a = [(1,2),(2,3),(4,5)]

a.sort(key=lambda x : x[1])
print(a)