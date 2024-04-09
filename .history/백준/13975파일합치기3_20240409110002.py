'''
입력값 100만 + 최소비용 + 시간제한2초 아마 이진탐색일듯?
left, right, 기준 정하는게 문제인데
left = sum(files), right = sum(files) * 3 < 이건 상황따라 늘려도될듯
정렬해도 상관 없고
mid가 초가 되면

'''
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    K = int(input())
    files = list(map(int,input().split()))
    #여기에 최소값 계산해서 출력하는 로직



