'''
BFS그대로 구현
'''
import sys
input = sys.stdin.readline
def bfs(idx):
    global cnt
    queue = []
    queue.append(idx)
    visited[idx]+=cnt
    while queue:
        cur = queue.pop(0)
        for i in sorted(graph[cur]):
            if visited[i]==0:
                cnt+=1
                queue.append(i)



N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
cnt = 1

bfs(R)

for i in range(1,N+1):
    print(visited[i])