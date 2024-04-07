from heapq import *

a = [(2,3),(1,2),(4,5)]
b = [[4,6],[1,2],[2,3]]
a.sort(key=lambda x :x[1])
print(a)
b.sort()
print(b)