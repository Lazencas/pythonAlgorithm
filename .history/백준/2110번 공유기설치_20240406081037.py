# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
'''
왼쪽거리, 오른쪽거리 비교는 좋은데 언제 멈춰야하지?
다 기록해서 뽑자, 뽑는 기준
둘 값 비교해서 더 큰값이 뒤로가게 하는 튜플 만들고 리버스정렬해서 0번인덱스 뽑자
'''
import sys
input = sys.stdin.readline
N, C = map(int,input().split())
house_list=[]
for i in range(N):
    house = int(input())
    house_list.append(house)
house_list.sort()
left = 0
right = N-1
i=0
ans  = []
while left<=right:
    mid = (left+right)//2
    #왼쪽거리 오른쪽거리
    left_len, right_len = 0,0
    #왼쪽에서 mid인덱스거리, mid인덱스에서 오른쪽 거리
    left_len = house_list[mid]-house_list[left]
    right_len = house_list[right]-house_list[mid]
    # print('left, right',left_len,'+',right_len)
    if left_len>= right_len:
        ans.append([right_len,left_len])
    else:
        ans.append([left_len,right_len])

    if left_len <= right_len:
        right = mid-1
    else :
        left = mid+1
    i+=1
    # print('몇번돌앗게',i)

ans.sort(reverse=True)
print(ans[0][0])
