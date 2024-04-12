'''
0.5초, 128MB
도시 1~N번까지, 반복문N번 하고 인덱스+1
다익스트라 그대로 쓰면 될듯

이중 딕셔너리 구조 만드는데 시간 좀 듦

'''
import sys
from collections import defaultdict
from heapq import *
input = sys.stdin.readline
def dijkstra(start): 
    queue = []
    heapify(queue)
    heappush(queue,[distances[start], start])

    while queue:
        cur_dis, cur_city = heappop(queue)

        if cur_dis > distances[cur_city]:
            continue

        for adj,weight in city[cur_city].items():
            dist = cur_dis + weight

            if dist < distances[adj]:
                distances[adj]=dist
                heappush(queue,[dist,adj])

    return distances



N = int(input())
M = int(input())
city = defaultdict(dict)
for i in range(M):
    start, end, cost = map(int,input().split())
    city[start][end] = cost
start, end = 0, 0
start, end = map(int,input().split())
print(start, end)

distances = {i+1:float('inf') for i in range(N)}
distances[start] = 0

print(dijkstra(start))

