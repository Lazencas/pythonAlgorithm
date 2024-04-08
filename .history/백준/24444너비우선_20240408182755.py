'''
BFS그대로 구현
'''
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)