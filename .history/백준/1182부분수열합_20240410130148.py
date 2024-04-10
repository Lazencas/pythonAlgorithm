'''
시간제한2초, 256MB
S는 -100만~100만, 정수개수는 20개 이하, 주어지는 정수 -10만~10만
따로 있는 양의 수열들 구분해서 각 수열들에서 경우의 수 구해서 다 더해야겠다.

크기가 양수인 부분수열이라는 말이 이해가 잘안가서 헤맴

'''
import sys
input = sys.stdin.readline
from collections import *
from itertools import * 
plus = []
N, S = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in range(1,N+1):
    a = combinations(l,i)
    print(a)