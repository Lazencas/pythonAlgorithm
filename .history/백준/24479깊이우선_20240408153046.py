'''
의사코드 확인하면서 DFS방식으로 코드 짜면 될듯
'''
import sys
input = sys.stdin.readline

def dfs(idx):
    if visited[idx]:
        return
    visited[idx]=True
    graph[idx].sort()
    for i in graph[idx]:
        if visited[i]==False:
            visited[i]=True
            dfs(i)

N, M, R = map(int,input().split())
graph =  [[] for i in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)
dfs(R)
for i in range(1,N+1):
    print(visited[i])

