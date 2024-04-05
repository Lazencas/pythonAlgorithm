# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 입력
# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 제한
# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109
'''
입력 100만 이하 N개, 시간제한 2초 메모리512MB
>> 자기 값보다 작은 서로다른 수의 개수 = 곧 자기의 수 > 다 이렇게 바꿔야 함
정렬하면 안되나? 순서 바뀌는 거 처리가능하면야 상관없는데 너무 복잡하지 않나?
일단 튜플넣고 정렬해보자
인덱스 따지는거랑 값 따지는 거랑 헷갈리는 듯

'''
from collections import *
import sys
input = sys.stdin.readline
N = int(input())
x = [(i,idx) for idx,i in enumerate(map(int,input().split()))]
x.sort()
print(x)
left = 0
right = N-1
his = defaultdict(int)
# 같은 수 있으면 줄여야하는데
for i in range(N):
    if his[x[i][0]] !=0:
        x[i] = list(x[i])
        x[i][0] = his[x[i][0]]
        x[i]= tuple(x[i])
    else:
        #이진탐색, 자기x[i][0]보다 작은 수 개수 찾기
        while left <= right:
            cnt = 0
            mid = (left+right)//2
            if x[mid][0] == x[i][0]:
                right = mid-1
            elif x[mid][0] > x[i][0]:
                right = mid-1
            else:
                left = mid+1
                cnt+=1
        x[i] = list(x[i])
        x[i][0] = cnt
        x[i]= tuple(x[i])
        his[x[i][0]] = cnt
print(x)
