'''
1초,128MB

'''
import sys
from sys import *
setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global cnt
    if visited[idx]:
        return
    visited[idx]=True
    for i in graph[idx]:
        dfs(i)


N = int(input())
S = int(input())
graph = [[] for i in range(N+1)]
for i in range(S):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False]*(N+1)
cnt =0
dfs(1)
print(cnt)