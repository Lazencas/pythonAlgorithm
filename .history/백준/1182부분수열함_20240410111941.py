'''
시간제한2초, 256MB
S는 -100만~100만, 정수개수는 20개 이하, 주어지는 정수 -10만~10만
따로 있는 수열들 구분해서 각 수열들에서 경우의 수 구해서 다 더해야겠다.

'''
import sys
input = sys.stdin.readline
N, S = map(int,input().split())
plus = list(map(int,input().split()))
print(plus)