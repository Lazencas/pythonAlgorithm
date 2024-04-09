'''
어떻게 최소 값이 되는지 감이 안잡힘
구현식으로 가보자
시간초과.....
'''
import sys
from collections import *
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])
    while queue:
        n = queue.popleft()
        if n == K:
            return array[n]
        for next_n in (n-1, n+1, 2*n):
            if 0<= next_n < max and not array[next_n]:
                array[next_n] = array[n] + 1
                queue.append(next_n)


cnt=0
N, K = map(int,input().split())
max = 100000
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