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

# a = [[1,2],[2,3],[4,5],[6,7]]
# b=a[:a[0]]
# print(b)

def dfs(idx):
    stack = []
    stack.append(idx)
    while stack:
        current = stack.pop()
        print(f"{current} 방문맨")
        visited[current] = True
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                visited[i]=True

def bfs(idx):
    stack = []
    stack.append(idx)
    while stack:
        current = stack.pop(0)
        print(f"{current} 방문햇어")
        visited[current] = True
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
'''
def dfs(idx):
    if visited[idx]:
        return
    visited[idx]=True
    print(f"{idx}방문")
    for i in graph[idx]:
        dfs(i)
'''
n = 7
graph = [[] for i in range(n+1)]
graph[1].append(2)
graph[1].append(3)
graph[2].append(4)
graph[2].append(5)
graph[3].append(6)
graph[3].append(7)
visited = [False] * (n+1)
# print(graph)
dfs(1)