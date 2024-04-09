'''
어떻게 최소 값이 되는지 감이 안잡힘
구현식으로 가보자
'''
import sys
input = sys.stdin.readline
ans = []
cnt=0
N, K = map(int,input().split())
#자기의 2배가 동생을 넘기 전까지 2개 반복
while N*2 < K:
    N*=2
    cnt+=1
    print(N)

#여기서 각 경우의수를 나눈다
#목표값 까지 하나 씩 앞으로 걸어가는 경우
cnt_1 = 0+ cnt
while N==K:
    N+=1
    cnt_1 += 1
print(cnt_1)