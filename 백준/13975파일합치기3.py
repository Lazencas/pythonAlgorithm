'''
입력값 100만 + 최소비용 + 시간제한2초 아마 이진탐색일듯?
left, right, 기준 정하는게 문제인데
left = sum(files), right = sum(files) * 3 < 이건 상황따라 늘려도될듯
이진탐색으로 하기에는 뭔가 시간이 늘고 줄어드는 기준을 모르겠음
이진탐색 아닌듯

정렬해도 상관 없고

mid가 초가 되면- 그냥 최소 힙써서 최소 값뽑아서 계산하면
최소값 될거같음 -> 아님

어떻게 하면 시간이 줄어드는지를 알아야 하는데 그걸 모르겠음
최소값 + 최대값 매칭이 제일 적은 시간인가? -> 아님

모든 더하는 경우의 수 다 구한다음에 그 중에서 최소 값 구해야 하나본데
근데 경우의 수랑 bfs, dfs 접목하는거 할 줄 모르는데 어떻게 푸냐

너무 문제가 시험 전날 범위에 치중되어서 나오는데 
오늘 같은 경우 그래프 탐색문제가 많은거 같은데 못해도 4문제중에 2개는 되는거같음

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
    for i in file:
        files.append(i)
    print(files)
    cnt = 0
    for i in range(len(files)-1):
        a = files.popleft()
        b = files.pop()
        c = a+b
        cnt+=c
        files.append(c)
    print(cnt)

