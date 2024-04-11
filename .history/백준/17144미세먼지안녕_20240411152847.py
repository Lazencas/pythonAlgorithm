'''
시간제한 1초, 메모리512MB
집 크기 R*C 6이상 50미만 시간T는 1초이상 1000초 이하

1.미세먼지가 확산되는 함수 (시간T,R*C집리스트) 반환값 > 확산된 결과의 house
2.공기청정기가 작동하는 함수 (시간T,R*C집리스트)
3.미세먼지의 양을 구하는 함수 (R*C집리스트)

'''
import sys
input = sys.stdin.readline
#미세먼지가 확산되는 함수
#순차 탐색 하면서 숫자만나면 < 이거 문제생김
#해당 숫자의 전후좌우를 확인함
#막혀있거나 -1을 만나면 확산 안함
#확산 가능한 칸을 모두 세고, //5 한 값을 칸의 수로 나누고
#각 칸에 해당 몫을 나눠주고 자기 자신 값에서 그만큼 뺀다
def spread():
    #먼지 중복확산을 방지하기위해 복사본 준비하고 공기청정기 배치
    copy_house = [[0]*C for _ in range(R)]
    copy_house[up][0]= -1
    copy_house[down][0]= -1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(R):
        for j in range(C):
            if house[i][j] > 0:
                copy_house[i][j] += house[i][j]
                #확산방향인 4방향 체크
                for k in range(4):        
                    mi = i + dx[k]
                    mj = j + dy[k]
                    if R> mi >= 0 and C > mj >= 0 and house[mi][mj] != -1:
                        copy_house[mi][mj] += house[i][j] // 5
                        copy_house[i][j] -= house[i][j] // 5
    return copy_house

#값을 옮기면서 중복되서 값이 이상하게 나오는거 발견하고 고치는데 시간이 많이 듬
def cycle():
    #공기청정기 up부분에서 나타나는 반시계방향 순환(채우는건 반대로)
    #공기 청정기 바로 위칸 부터 시작 ↑
    for i in range(up-1, 0, -1):
        house[i][0] = house[i-1][0]
    # →
    for i in range(C-1):
        house[0][i] = house[0][i+1]
    # ↓
    for i in range(up):
        house[i][-1] = house[i+1][-1]
    # ←
    for i in range(C-1, up, -1):
        house[up][i] = house[up][i-1]

    #공기청정기 down부분에서 나타나는 시계방향 순환(채우는건 반대로)
    #공기청정기 바로 아래칸 부터 시작 ↓
    for i in range(down+1, R-1):
        house[i][0] = house[i+1][0]
    # →
    for i in range(C-1):
        house[-1][i] = house[-1][i+1]
    # ↑
    for i in range(R-1, down, -1):
        house[i][-1] = house[i-1][-1]
    # ←
    for i in range(C-1, 0, -1):
        house[down][i] = house[down][i-1]

    #공기청정기에서 나온 바람
    house[up][1] = 0
    house[down][1] = 0

def result(house):
    total = 0
    for i in range(len(house)):
        for j in range(len(house)):
            total += house[i][j]
    return total + 2

house = []
R, C, T = map(int,input().split())
for i in range(R):
    rc = list(map(int,input().split()))
    house.append(rc)

#공기청정기 위치 찾기
for i in range(R):
    if house[i][0]==-1:
        up, down = i, i+1
        break
for i in range(T):
    house = spread()
    cycle()
print(result(house))

