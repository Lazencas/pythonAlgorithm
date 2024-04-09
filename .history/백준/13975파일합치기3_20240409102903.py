'''
입력값 100만 + 최소비용 + 시간제한2초 아마 이진탐색일듯?
left, right, 기준 정하는게 문제인데
'''
import sys
input = sys.stdin.readline
T = int(input())
file = []
for i in range(T):
    K = int(input())
    files = list(map(int,input().split()))
    file.append(files)
print(file)
