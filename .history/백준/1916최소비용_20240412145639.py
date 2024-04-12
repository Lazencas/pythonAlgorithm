'''
0.5초, 128MB
도시 1~N번까지, 반복문N번 하고 인덱스+1
다익스트라 그대로 쓰면 될듯
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
M = int(input())
city = defaultdict(dict)
for i in range(M):
    start, end, cost = map(int,input().split())
    city[start][end] = cost
        
print(city[1])