'''
2초, 128MB
회의 수 N 10만 이하, 각 회의 시간 주어짐
겹치지 않게 하면서 사용하는 회의의 최대 개수.

최소힙으로 시작시간 기준으로 뽑으면 될거같은데< 이럼 안되고
(end-start + 자기 인덱스 값) 이게 가중치? 낮은 순서대로 정렬해서 뽑으면 될듯?
그 값이 같으면 인덱스 값이 낮은 순서대로 정렬

그 낮은 순서에서 자기 end값보다 가려는 값의 start값이 같거나 커야함 

회의 걸리는 시간을 계산했는데, 사실 끝나는 시간이랑 시작하는 시간만 따져도 됨

'''
import sys
from collections import *
from heapq import *
input = sys.stdin.readline
N = int(input())
time = []

for i in range(N):
    start, end = map(int,input().split())
    time.append([end,start])

time.sort()
ans = 0
endtime = 0

for i in time:
    print(i)
    if i[1] >= endtime:
        ans+=1
        endtime = i[0]


print(ans)
