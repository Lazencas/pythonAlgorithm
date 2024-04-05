# 문제
# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다.
#  정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 
#  나무를 구할것이다.

# 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 
# 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 
# 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 
# 예를 들어, 한 줄에 연속해있는 나무의 높이가
#  20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 
# 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고
#  , 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 
# 절단기에 설정할 수 있는
#   높이는 양의 정수 또는 0이다.

# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. 
# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 
# 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

# 출력
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

'''
M을 만족하는 최소값을 구해야 함.
N은 100만 이하, M은 20억 이하고 시간제한 1초. 
N이 100만이니 이중 반복문 사용 불가.
이진 탐색은 정렬 되어 있어야 하니 추가로 정렬도 필요하나?
min, max 함수도 못쓰는데, 최소값 최대값 없이 되나?
종료조건이 이상한데..... 적절한 종료 조건을 못찾겟는데
+1, -1 뺏더니 무한루프 못고치네, 그냥 넣자
'''
import sys
input = sys.stdin.readline
N, M  = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
left = trees[0]
right = trees[N-1]
ans = []
mid = (left+right)//2

#이진탐색
while left<=right:
    tmp = 0
    for i in range(N):
        if (trees[i]-mid) > 0:
            tmp += (trees[i]-mid)
    
    #조건을 만족 할 때, mid값을 키워나감
    if tmp >= M:
        ans.append(mid)
        left = mid+1

    #길이 미달, mid값을 줄여야함
    else:
        right = mid-1
    mid = (left+right)//2

if len(ans)>1:
    print(max(ans))
else:
    print(*ans)