'''
1초 512MB
N명 키순, K개의조
N 30만 이하
티셔츠 비용 = 가장키큰-가장작은
이 비용의 합을 최소로.

어떨 때 비용이 최소가 되는가?
일단 순서는 안바뀜. 
'''
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
h = list(map(int,input().split()))
