'''
정사각형 이차원배열, 자기위의 수보다 큼 -> 0번인덱스일때는 예외, 그외에는 -i번 인덱스보다 큼
전체에서 N번째 큰수를 찾으려면

1500이 최대 값이니, 이중 반복문 + 적당한 반복문 정도면 됨
heap에 넣어서 몇번째 나왔는지 체크하면 그게 답인데
입력으로 다 힙에다 쳐 넣고 N번 뽑아보자 1500*1500 >> 메모리초과 나오는데?;;

.....워떡하누.....
쓴거 지우자 > 안되고
받아서 리스트에 안넣고 바로 힙푸쉬 하면 될거같은데> 안됨
값을 다 받으면 안되나 본데

저장 안하고 바로바로 처리해야 함
N까지의 크기만 유지하고 heap리스트의 [0]번보다 크면 그걸로 바꿈
그러면 heap리스트의 [0]번은 항상 N번째의 크기를 유지 할 수 있음
'''
import sys
from heapq import *
input = sys.stdin.readline
n_list=[]
heap_list = []
heapify(heap_list)
n = int(input())
for i in range(n):
    a = map(int,(input().split()))
    for j in a:
        #메모리 절약을 위해 크기제한
        if len(heap_list) < n:
            heappush(heap_list, j)
        else:
            if heap_list[0] < j:
                heappop(heap_list)
                heappush(heap_list,j)
print(heap_list[0])




   
