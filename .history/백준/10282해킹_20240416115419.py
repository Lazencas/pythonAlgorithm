'''
2초 256MB
총 몇대가 감염되고 얼마나 시간이 걸리는지 구하는 문제
그래프를 초기화 하고, 그 그래프에서 감염시키고나서 몇대 감염되고 시간 카운트한거 반환

'''
import sys
from collections import *
input = sys.stdin.readline
net = defaultdict(dict)
T = int(input())
for _ in range(T):
    #컴퓨터개수 n, 의존성개수d, 해킹당한컴c
    n,d,c = map(int,input().split())
    for _ in range(d):
        #a,b,s s초 후 b가 감염되면 a가 감염됨
        end, start, sec = map(int,input().split())
        net[start][end] = sec
    print(net)