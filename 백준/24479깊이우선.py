'''
의사코드 확인하면서 DFS방식으로 코드 짜면 될듯
순서랑 해당 줄을 몇번재 방문했는지 출력하는거랑 헷갈림

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

N, M, R = map(int,input().split())
graph =  [[] for _ in range(N+1)]
# visited = [False]*(N+1)
visited = [0]*(N+1)
cnt = 1

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)
for i in range(1,N+1):
    print(visited[i])

#틀린부분
# for i in range(1,N+1):
#     if visited[i]!=0:
#         print(int(i))
#     else:
#         print(int(0))
