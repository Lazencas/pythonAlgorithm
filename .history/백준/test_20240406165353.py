# from heapq import *

# a = [(2,3),(1,2),(4,5)]
# b = [[4,6],[1,2],[2,3]]
# a.sort(key=lambda x :x[1])
# print(a)
# b.sort()
# print(b)


# x,y=map(int,input().split()) 
# z=(100*y)//x 
# left=0 
# right=x 
# res=x 
# if z>=99: 
#     print(-1)
# else: 
#     while left<=right: 
#         mid=(left+right)//2 
#         if (100*(y+mid))//(x+mid)>z: 
#             res=mid 
#             right=mid-1 
#         else: 
#             left=mid+1
#     print(res)

a = [[1,2],[2,3],[4,5],[6,7]]
b=a[:a[0]]
print(b)