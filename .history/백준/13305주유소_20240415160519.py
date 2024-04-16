'''
시간제한2초, 512MB
도시의개수 N 10만이하, 제일 왼쪽~제일 오른쪽 도시까지는 10억 이하
최소비용 구하기

모든 경우의 수를 따져야 하니 DFS;BFS;사용,
그렇기에는 도시개수가 10만개 까지 가서 최적화를 해야함
중복되는 계산이 많아보임. 결국 DP인거 같은데......
'''
import sys
input = sys.stdin.readline
dp = [0]*100001
N = int(input())
d = list(map(int,input().split()))
oil = list(map(int,input().split()))