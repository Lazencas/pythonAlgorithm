# 문제
# 김형택은 지금 몰래 Spider Solitaire(스파이더 카드놀이)를 하고 있다. 형택이는 이 게임을 이길 때도 있었지만, 
# 질 때도 있었다. 누군가의 시선이 느껴진 형택이는 게임을 중단하고 코딩을 하기 시작했다. 
# 의심을 피했다고 생각한 형택이는 다시 게임을 켰다. 그 때 형택이는 잠시 코딩을 하는 사이에 자신의 게임 실력이 눈에 띄게 
# 향상된 것을 알았다.

# 이제 형택이는 앞으로의 모든 게임에서 지지 않는다. 하지만, 형택이는 게임 기록을 삭제 할 수 없기 때문에, 
# 자신의 못하던 예전 기록이 현재 자신의 엄청난 실력을 증명하지 못한다고 생각했다.

# 게임 기록은 다음과 같이 생겼다.

# 게임 횟수 : X
# 이긴 게임 : Y (Z%)
# Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
# X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

# 입력
# 각 줄에 정수 X와 Y가 주어진다.

# 출력
# 첫째 줄에 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.

# 제한
# 1 ≤ X ≤ 1,000,000,000
# 0 ≤ Y ≤ X
'''
입력 게임횟수 10억회....;; 프로게이머도 너보단 게임 적게 했겠다
한판이 1초 걸린다고 하면 총 플레이 시간 10억초 >> 하루가 86400초 >>10억초면 11574일 >> 31.7년
한판이 1초만 걸려도 카드게임을 31.7년동안 한건데 한판이 1초만에 끝날리가 없다.
카드게임이 1분걸린다고 치면 >> 1902년동안 스파이더 카드게임을 한 사람(사람아닌듯).....

시간초과 걸리는데.... 시간을 어떻게 줄이지.....
푸는 방법을 바꿔야하나

이진탐색 될거 같은데? 값이 바뀌는 최소값? 
left = 1, right = X, mid = (left+right)//2
mid값으로 Z값이 변하면 right = mid-1
안변하면 left = mid+1

됫는데 가끔 1이 오차가 나는데 왜그렇지?

'''
import sys
input = sys.stdin.readline
X, Y = map(int,input().split())
Z = (100*Y/X)
old = (100*Y/X)
left, right = 0,X
ans = []
if Z >= 100:
    print(-1)
else:
    while left <= right:
        #mid값 구하고 X랑 Y에 계속 mid값 더하면서 승률Z가 변하는지, 변하면 그 값중 최소값
        newX, newY = X, Y
        mid = (left+right)//2
        newX+=mid
        newY+=mid
        Z = (100*(newY)//newX)
        #Z가 변하는지만 체크하면 되니까 여기 if문을 좀 변형했는데 여기서 이상한건가?
        #Z가 안변하면 무조건 mid값을 늘려야 하니까 원본값old랑 변한 값 Z비교해서
        #같으면 left = mid+1
        
        if Z>old:
            #Z를 변하게 한 mid값 일단 리스트에 저장하고 최소값 찾기 위해 mid줄여나감
            ans.append(mid)
            right = mid-1
        else:
            left = mid+1


    print(min(ans))