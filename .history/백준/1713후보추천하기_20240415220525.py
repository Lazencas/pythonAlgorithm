'''
시간제한 2초, 128MB
추천횟수 1000번이하, 학생은 1~100
기존의 히스토리를 관리하면서 쭉가는 형태라, 스택사용할거 같다.

학생들이 추천을 시작하기전 사진들은 비어있고 > 스택 만들고, 이 스택의 크기는 고정(N개)
1.추천 받으면 그 학생은 게시되어야한다 > 스택에 반드시 들어가야한다.
2.자리가 없으면  추천을 가장 적게 받은 사진을 삭제하고 추가 > 추천수 최소힙해서 버려버리면될듯
같다면 게시된지 오래된 사진 -> 최소힙에서 들어온 순서도 고려하나? 고려안함
그러면 deque으로 구현 해야한다 > 추가되면 append하고 오래된건 인덱스 작은거
추천받은게 사진에 있으면 추천수 +
사진 삭제되면 추천수 0

답인 덱 오름차순 정렬

이차원배열로 하고 [후보,추천수,들어온 순서] 이렇게 
추천수는 딕셔너리로 따로 관리


'''
import sys
from collections import *
input = sys.stdin.readline
N = int(input())
r = int(input())
s = list(map(int,input().split()))
rec = defaultdict(int)
photo = [[0,0,0]]*N
print(photo)
for i,s in enumerate(s):
    for j in range(len(photo)):
        print('check',j)
        print(photo)
        #해당 후보가 있을때 추천수+1
        if s == photo[j][0]:
            photo[j][1]+=1
            break
        else:
            #해당 후보가 없고 크기가 안넘을때
            if len(photo)<N:
                photo.append([s,1,i])
                break
            #해당 후보가 없고 크기가 같거나 넘을 때
            #추천수 낮고, 들어온 순서 낮은거 팝 >둘다 내림차순 하고 팝
            else:
                photo.sort(key= lambda x:(-x[1],-x[2]))
                photo.pop()
                photo.append([s,1,i])
                break
for a,b,c in photo:
    print(a)