'''
2초 256MB
총 몇대가 감염되고 얼마나 시간이 걸리는지 구하는 문제
그래프를 초기화 하고, 그 그래프에서 감염시키고나서 몇대 감염되고 시간 카운트한거 반환

더 빠른경로가 있을 경우를 생각 못했네
이럼 bfs가 아니라 다익스트라 썻지;

언제 최소값을 쓰고, 언제 값을 더해야 할지 구분식을 못세우겠다.> 이거아님 그냥
가장 큰 값임

인덱스에러 못찾겟는데...
아..... 딕셔너리 초기화를 반복문 밖에서 해가지고, 전에 했던
테스트케이스가 안지워져서 키에러, 인덱스아웃오브레인지... 같은 난리가
났던거네.... 이거 오류 찾는데 걸린시간 대략 4시간.....
예제 맞는데 다른 테스트케이스 칼같이 틀리는경우는 반복문이랑 초기화
살펴보자
'''
import sys
from collections import *
from heapq import *
input = sys.stdin.readline
def dijkstra(start):
    dist[start]=0
    q = []
    heapify(q)
    heappush(q,[dist[start],start])

    while q:
        cur_dis, cur = heappop(q)

        if cur_dis > dist[cur]:
            continue

        for adj,sec in net[cur].items():
            dis = sec + cur_dis

            if dis < dist[adj]:
                dist[adj]= dis
                heappush(q,[dis,adj])


T = int(input())
for _ in range(T):
    #컴퓨터개수 n, 의존성개수d, 해킹당한컴c
    n,d,c = map(int,input().split())
    net = defaultdict(dict)
    total_sec = 0
    hacked_pc = 0
    dist = {i:float('inf') for i in range(n+1)}
    for _ in range(d):
        #a,b,s s초 후 b가 감염되면 a가 감염됨
        end, start, sec = map(int,input().split())
        net[start][end] = sec


    dijkstra(c)
    for key, value in dist.items():
        if value != float('inf'):
            hacked_pc+=1
        if value == float('inf'):
            dist[key] = 0

    total_sec = max(dist.values())
    print(f"{hacked_pc} {total_sec}")