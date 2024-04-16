'''
시간제한1초, 128MB
N 5만개 이하 헛간, M개의 양방향 길 5만 이하,각각의 길은 1000마리 이하 소
1에서 N
가중치가 있는 그래프에서 최소가중치면 다익스트라 쓰면 될거같은데

'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
for i in range(M):
    start, end, cost = map(int,input().split())