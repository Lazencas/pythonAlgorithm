'''
시간제한2초, 512MB
도시의개수 N 10만이하, 제일 왼쪽~제일 오른쪽 도시까지는 10억 이하
최소비용 구하기

모든 경우의 수를 따져야 하니 DFS;BFS;사용,
그렇기에는 도시개수가 10만개 까지 가서 최적화를 해야함
중복되는 계산이 많아보임. 결국 DP인거 같은데......

이진탐색인거 같기도하고

total = 0잡고, 도시 기름값 최소힙큐에 넣고, 거기서 최소값*거리 만큼 비용을 더해나가면
그게 최소값
그리디 + 최소힙 문제인거같다.
'''
import sys
from heapq import *
input = sys.stdin.readline
dp = [0]*100001
N = int(input())
d = list(map(int,input().split()))
oil = list(map(int,input().split()))
total = 0
print(oil)
min_oil =[]
heapify(min_oil)
heappush(min_oil,oil[0])

for i in range(N-1):
    total+=(d[i]*min_oil[0])
    heappush(min_oil,oil[i+1])

print(total)
