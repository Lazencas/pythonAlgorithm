'''
어떻게 최소 값이 되는지 감이 안잡힘
구현식으로 가보자
시간초과.....
최단 시간 ~ BFS, DFS
세가지 방법 x+1 x-1 x*2  곧 3가지 노드
어떤게 최적값이 모르니 너비우선 탐색이 적당하다.

'''
import sys
from collections import *
input = sys.stdin.readline

def bfs(n):
    #시작점 수빈이 위치 N
    queue = deque([n])
    while queue:
        #bfs 니까 큐 자료구조 사용 위해 덱 사용
        n = queue.popleft()
        #K의 위치랑 같으면 해당 값 반환
        if n == K:
            return array[n]
        for next_n in (n-1, n+1, 2*n):
            if 0<= next_n < max and not array[next_n]:
                array[next_n] = array[n] + 1
                queue.append(next_n)


cnt=0
N, K = map(int,input().split())
max = 100001
#했던거 체크하기 위한 자료구조
array = [0] * max
print(bfs(N))









'''
new_N = N
#자기의 2배가 동생을 넘기 전까지 2개 반복
while new_N*2 < K:
    new_N*=2
    cnt+=1
fN = new_N

if fN*2 == K:
    cnt+=1
    print(cnt)
else:
    #여기서 각 경우의수를 나눈다
    #1.목표값 까지 하나 씩 앞으로 걸어가는 경우
    if (K-fN) <= (fN//2):
        cnt_1 = 0+ cnt
        while new_N!=K:
            new_N+=1
            cnt_1 += 1
        ans.append(cnt_1)
    #2.목표값을 앞지르고 거기서 빼는 경우
    if ((fN*2) - K) <= (fN//2):
        new_N2 = fN
        new_N2 = new_N2*2
        cnt_2 = 1 + cnt
        while new_N2!=K:
            new_N2-=1
            cnt_2+=1
        ans.append(cnt_2)
    #3.해당값의 배수까지 값을 조절하고 순간이동하고 다시 조정하는 경우
    new_N3 = fN
    cnt_3 = 0+cnt
    #new_N3에서 빼다가 반값보다 작아지면 스탑
    while K/2 < new_N3-1:
        cnt_3 += 1
        new_N3-=1
    new_N3 = new_N3*2
    cnt_3+=1
    while K!= new_N3:
        cnt_3+=1
        new_N3-=1
    ans.append(cnt_3)
    print(min(ans))
'''