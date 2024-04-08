'''
의사코드 확인하면서 DFS방식으로 코드 짜면 될듯
틀렷다는데 어디가 틀린건지 확인 불가

'''
import sys
from sys import *
input = sys.stdin.readline
setrecursionlimit(10 ** 6)

def dfs(idx):
    global cnt
    visited[idx]=cnt
    for i in sorted(graph[idx]):
        if visited[i]==0:
            cnt+=1
            dfs(i)

    '''
    if visited[idx]:
        return
    visited[idx]=True
    for i in sorted(graph[idx]):
        if not visited[i]:
            dfs(i)
    '''
N, M, R = map(int,input().split())
graph =  [[] for _ in range(N+1)]
# visited = [False]*(N+1)
visited = [0]*(N+1)

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)
for i in range(1,N+1):
    print(visited[i])

# for i in range(1,N+1):
#     if visited[i]:
#         print(i)
#     else:
#         print(0)
