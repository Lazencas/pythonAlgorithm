'''
1초,128MB

'''
import sys
input = sys.stdin.readline

N = int(input())
S = int(input())
graph = [[] for i in range(N+1)]
for i in range(S):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)