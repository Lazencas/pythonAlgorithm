'''
1초 512MB
N명 키순, K개의조
N 30만 이하
티셔츠 비용 = 가장키큰-가장작은
이 비용의 합을 최소로.

어떨 때 비용이 최소가 되는가?
일단 순서는 안바뀜.
5개중에 3개 뽑는 모든 경우의 수, 근데 이 뽑는게 
'''
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
h = list(map(int,input().split()))

array = []
for i in range(1,N):
    array.append(h[i]-h[i-1])

array.sort(reverse=True)
print(sum(array[K-1:]))
