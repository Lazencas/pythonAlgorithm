'''
의사코드 확인하면서 DFS방식으로 코드 짜면 될듯
출력초과 나오는데.....

'''
import sys
from sys import *
input = sys.stdin.readline
setrecursionlimit(10 ** 6)

def dfs(idx): 
    if visited[idx]:
        return
    visited[idx]=True
    for i in graph[idx]:
        if visited[i]==False:
            dfs(i)

N, M, R = map(int,input().split())
graph =  [[] for i in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(R)
for i in range(1,N+1):
    if visited[i]:
        print(i)
    else:
        print(0)

