'''
의사코드 확인하면서 DFS방식으로 코드 짜면 될듯
'''
import sys
input = sys.stdin.readline

def dfs(idx):
    if visited[idx]:
        return
    print(idx)
    visited[idx]=True
    for i in graph[idx]:
        dfs(i)

N, M, R = map(int,input().split())
graph =  [[] for i in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(len(graph)):
    graph[i].sort(reverse=True)
dfs(R)

