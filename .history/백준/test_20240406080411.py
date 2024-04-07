from heapq import *

a = [(2,3),(1,2),(4,5)]

a.sort(key=lambda x :x[1])
print(a)