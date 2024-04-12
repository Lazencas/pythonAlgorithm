'''
2초, 128MB
회의 수 N 10만 이하, 각 회의 시간 주어짐
겹치지 않게 하면서 사용하는 회의의 최대 개수.

최소힙으로 시작시간 기준으로 뽑으면 될거같은데< 이럼 안되고
(end-start + 자기 인덱스 값) 이게 가중치? 낮은 순서대로 정렬해서 뽑으면 될듯?
그 값이 같으면 인덱스 값이 낮은 순서대로 정렬

그 낮은 순서에서 자기 end값보다 가려는 값의 start값이 같거나 커야함 
'''
import sys
from collections import *
from heapq import *
input = sys.stdin.readline
N = int(input())
time = []

for i in range(N):
    start, end = map(int,input().split())
    time.append([start,end])

table = [[0] for _ in range(len(time))]
time.sort()
for i in range(len(time)):
    table[i] = [(time[i][1]-time[i][0]+i),time[i][0],time[i][1]]

ans = []
table.sort()
end = table[0][2]
ans.append(table[0])
print(ans)
for i in range(1,len(table)):
    if (table[i][2]+table[i][1])-1 <= i and table[i][2] >=end:
        ans.append(table[i])

print(ans)
