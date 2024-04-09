'''
어떻게 최소 값이 되는지 감이 안잡힘
구현식으로 가보자
'''
import sys
input = sys.stdin.readline
ans = []
N, K = map(int,input().split())
#자기의 2배가 동생을 넘기 전까지 2개 반복
while N*2 < K:
    print(N)