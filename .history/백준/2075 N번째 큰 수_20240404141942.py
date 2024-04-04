'''
정사각형 이차원배열, 자기위의 수보다 큼 -> 0번인덱스일때는 예외, 그외에는 -i번 인덱스보다 큼
전체에서 N번째 큰수를 찾으려면

1500이 최대 값이니, 이중 반복문 + 적당한 반복문 정도면 됨
heap에 넣어서 몇번째 나왔는지 체크하면 그게 답인데
입력으로 다 힙에다 쳐 넣고 N번 뽑아보자 1500*1500 >> 메모리초과 나오는데?;;

.....워떡하누.....
쓴거 지우자

'''
import sys
from heapq import *
input = sys.stdin.readline
n_list=[]
heap_list = []
heapify(heap_list)
n = int(input())
for i in range(n):
    a = list(map(int,(input().split())))
    n_list.append(a)
    del a

for i in range(len(n_list)):
    for j in n_list[i]:
        #몇번째 큰수 인지 꺼내야하니 -붙임
        heappush(heap_list, -(j))
ans=0
for i in range(n):
    ans = -(heappop(heap_list))

print(ans)



   
