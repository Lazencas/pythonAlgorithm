'''
입력값 100만 + 최소비용 + 시간제한2초 아마 이진탐색일듯?
left, right, 기준 정하는게 문제인데
left = sum(files), right = sum(files) * 3 < 이건 상황따라 늘려도될듯
이진탐색으로 하기에는 뭔가 시간이 늘고 줄어드는 기준을 모르겠음

정렬해도 상관 없고
mid가 초가 되면- 그냥 최소 힙써서 최소 값뽑아서 계산하면
최소값 될거같음 -> 아님

어떻게 하면 시간이 줄어드는지를 알아야 하는데 그걸 모르겠음
최소값 + 최대값 매칭이 제일 적은 시간인가?

'''
import sys
from collections import *
from heapq import *
input = sys.stdin.readline
files = deque()
ans = []
ans = heapify(ans)
T = int(input())
for i in range(T):
    K = int(input())
    file = list(map(int,input().split()))
    #여기에 최소값 계산해서 출력하는 로직
    file.sort()
    files.append(file)
    print(files)
    cnt = 0
    for i in range(len(files)-1):
        a = files.popleft()
        b = files.pop()
        c = a+b
        cnt+=c
        files.append(c)
    print(cnt)

