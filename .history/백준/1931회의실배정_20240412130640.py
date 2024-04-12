'''
2초, 128MB
회의 수 N 10만 이하, 각 회의 시간 주어짐
겹치지 않게 하면서 사용하는 회의의 최대 개수.

최소힙으로 시작시간 기준으로 뽑으면 될거같은데
'''
import sys
from collections import *
from heapq import *
input = sys.stdin.readline
N = int(input())
time = []
heapify(time)

for i in range(N):
    start, end = map(int,input().split())
    heappush(time,[start,end])

print(time)