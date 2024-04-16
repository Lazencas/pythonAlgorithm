'''
2초, 128MB
좌표 절대값 100만 이하, 센서 M 만개 이하, 집중국 K 1000개이하
수신가능 영역의 길이의 합이 최소인 값, 센서가 같은 좌표일수도 있음
이러면 센서 맨 처음좌표에 밖은게 최악의 값이니까
이거 기준으로 해서 이진탐색 하면 되겟는데
사이값?

'''
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
loc = list(map(int,input().split()))
bet = []
for i in range(1,N):
    bet.append(abs(loc[i]-loc[i-1]))
print(bet)