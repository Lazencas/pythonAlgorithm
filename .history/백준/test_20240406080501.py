from heapq import *

a = [(2,3),(1,2),(4,5)]
b = [[1,2],[2,3],[4,6]]
a.sort(key=lambda x :x[1])
print(a)
b.sort()
print(b)