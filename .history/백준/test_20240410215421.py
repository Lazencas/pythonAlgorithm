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
'''
def dfs(idx):
    stack = []
    stack.append(idx)
    while stack:
        current = stack.pop()
        print(f"{current}방문!")
        visited[current]= True
        for adj in graph[current]:
            if not visited[adj]:
                stack.append(adj)


def bfs(idx):
    stack = []
    stack.append(idx)
    while stack:
        cur = stack.pop(0)
        print(f"{cur}방문!")
        visited[cur]=True
        for i in graph[cur]:
            if not visited[i]:
                stack.append(i)


def rdfs(idx):
    if visited[idx]:
        return
    print(f"{idx}방문!")
    visited[idx]=True
    for i in graph[idx]:
        rdfs(i)

n = 5
graph = [[] for i in range(n+1)]
graph[1].append(2)
graph[1].append(3)
graph[2].append(4)
graph[3].append(5)
# graph[3].append(6)
# graph[3].append(7)
visited = [False] * (n+1)
# print(graph)
bfs(1)
'''
# a = []
# a.append([3,4])

# b,c=a.pop()
# print(b,c)
# a = 8.5
# a=round(a,0)
# print(a)

'''
def combo(n,m):

    0~n-1 중에서 m개를 선택하는 조합을 구하는 함수

    def dfs(idx, stack):
        if len(stack)==m:
            result.append(stack[:])
            return
        for i in range(idx,n):
            if not visited[i]:
                visited[i]=True
                stack.append(i)
                dfs(i, stack)
                stack.pop()
                visited[i]=False

    visited = [False]*n
    result = []
    dfs(0,[])
    return result

cs = combo(5,3)
for c in cs:
    print(c)
'''
import copy

a = [1,2,3,4]
b = copy.copy(a)

b.append(6)

print(a)
print(b)
