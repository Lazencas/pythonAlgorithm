'''
시간제한 1초, 메모리512MB
집 크기 R*C 6이상 50미만 시간T는 1초이상 1000초 이하

1.미세먼지가 확산되는 함수 (시간T,R*C집리스트)
2.공기청정기가 작동하는 함수 (시간T,R*C집리스트)
3.미세먼지의 양을 구하는 함수 (R*C집리스트)

'''
import sys
input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

#미세먼지가 확산되는 함수
#순차 탐색 하면서 숫자만나면
#해당 숫자의 전후좌우를 확인함
#막혀있거나 -1을 만나면 확산 안함
#확산 가능한 칸을 모두 세고, //5 한 값을 칸의 수로 나누고
#각 칸에 해당 몫을 나눠주고 자기 자신 값에서 그만큼 뺀다
def spread(house):
    for i in range(R):
        for j in range(C):
            if house[R][C]:
                break



house = []
R, C, T = map(int(input().split()))
for i in range(R):
    rc = list(map(int,input().split()))
    house.append(rc)
print(house)