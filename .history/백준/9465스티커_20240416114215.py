'''
시간제한 1초, 256MB

스티커 점수 최대값, n 10만이하
두 변을 공유하지 않는 스티커 점수의 최대값

스티커 개수가 10만개라 
자기 주변 3개 합보다 큰애는 무조건 고르고 남은거중에
자기 주변 2개 합보다 큰애
그리고 가장 큰애 순으로 집으면 됨
고른애 주변 값들은 0으로 만들어줘야 계산 편함
'''
import sys
input = sys.stdin.readline
dx=[1,0,-1,0]
dy=[0,1,0,-1]

T = int(input())
for _ in range(T):
    sticker = []
    n = int(input())
    for _ in range(2):
        st = list(map(int,input().split()))
        sticker.append(st)
    #여기에 스티커 점수 최대값 구해서 출력하는 로직
    ans = []
    for i in range(2):
        for j in range(n):
            #i가 0일때 왼 아래 오
            if i == 0:
                #j==0이면 아래 오른쪽
                if j == 0:
                #범위 안넘고 주변 범위 합이 0이면 그건 무조건 뽑고
                #자기 주변 값의 합보다 큰애 뽑고 주변 0만들기
                    total = 0
                    total+=sticker[i][j+1]
                    total+=sticker[i+1][j]
                    if total==0 or total<sticker[i][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j+1]=0
                        sticker[i+1][j]=0
                elif j == (n-1):
                    #j가 끝이면 왼 아래
                    total = 0
                    total+=sticker[i][j-1]
                    total+=sticker[i+1][j]
                    if total==0 or total<sticker[i][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i+1][j]=0
                else:
                    #j가 중간일때 왼 아래 오
                    total = 0
                    total+=sticker[i][j-1]
                    total+=sticker[i][j+1]
                    total+=sticker[i+1][j]
                    if total==0 or total<sticker[i][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i][j+1]=0
                        sticker[i+1][j]=0

            else:
                #i가 1일때 왼 위 오
                if j == 0:
                #범위 안넘고 주변 범위 합이 0이면 그건 무조건 뽑고
                #자기 주변 값의 합보다 큰애 뽑고 주변 0만들기
                    total = 0
                    total+=sticker[i][j+1]
                    total+=sticker[i-1][j]
                    if total==0 or total<sticker[i][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j+1]=0
                        sticker[i-1][j]=0
                elif j == (n-1):
                    #j가 끝이면 왼 아래
                    total = 0
                    total+=sticker[i][j-1]
                    total+=sticker[i-1][j]
                    if total==0 or total<sticker[i][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i-1][j]=0
                else:
                    #j가 중간일때 왼 위 오
                    total = 0
                    total+=sticker[i][j-1]
                    total+=sticker[i][j+1]
                    total+=sticker[i-1][j]
                    if total==0 or total<sticker[i][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i][j+1]=0
                        sticker[i-1][j]=0
    for i in range(2):
        for j in range(n):
            if i == 0:
                #j==0이면 아래 오른쪽
                if j == 0:
                #범위 안넘고 주변 범위 합이 0이면 그건 무조건 뽑고
                #자기 주변 값의 합보다 큰애 뽑고 주변 0만들기
                    if sticker[i][j]>=sticker[i][j+1] and sticker[i][j]>=sticker[i+1][j] :
                        ans.append(sticker[i][j])
                        sticker[i][j+1]=0
                        sticker[i+1][j]=0
                elif j == (n-1):
                    #j가 끝이면 왼 아래
                    if sticker[i][j-1]<=sticker[i][j] and sticker[i][j]>=sticker[i+1][j]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i+1][j]=0
                else:
                    #j가 중간일때 왼 아래 오
                    if sticker[i][j-1]<=sticker[i][j] and sticker[i][j]>=sticker[i+1][j] and sticker[i][j]>=sticker[i][j+1]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i][j+1]=0
                        sticker[i+1][j]=0

            else:
                #i가 1일때 왼 위 오
                if j == 0:
                #범위 안넘고 주변 범위 합이 0이면 그건 무조건 뽑고
                #자기 주변 값의 합보다 큰애 뽑고 주변 0만들기
                    if sticker[i][j]>=sticker[i-1][j] and sticker[i][j]>=sticker[i][j+1] :
                        ans.append(sticker[i][j])
                        sticker[i][j+1]=0
                        sticker[i-1][j]=0
                elif j == (n-1):
                    #j가 끝이면 왼 아래
                    if sticker[i][j]>=sticker[i-1][j] and sticker[i][j]>=sticker[i][j-1]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i-1][j]=0
                else:
                    #j가 중간일때 왼 위 오

                    if sticker[i][j]>=sticker[i-1][j] and sticker[i][j]>=sticker[i][j+1] and sticker[i][j] >= sticker[i][j-1]:
                        ans.append(sticker[i][j])
                        sticker[i][j-1]=0
                        sticker[i][j+1]=0
                        sticker[i-1][j]=0
    for i in range(2):
        for j in range(n):
            if sticker[i][j] != 0:
                ans.append(sticker[i][j])
    print(sum(ans))

