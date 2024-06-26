# 문제
# 1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다.
#  단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 
#  종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.

# 우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 
# 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진
#  풍선은 빼고 이동한다.

# 예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀
#  있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다.
# 종이에 0은 적혀있지 않다.

# 출력
# 첫째 줄에 터진 풍선의 번호를 차례로 나열한다.

'''
풍선의 인덱스와 안에 들어있는 숫자를 같이 관리 해야하는데
0번부터 시작해서 나온 숫자만큼 이동하는데, 경계부분 어떻게 이동하지? -1번 인덱스가 끝이라서 그냥 그렇게 계산

이동 따지는건 하나씩 지워야하는데, 정답은 안지워진 풍선에서 인덱스+1 세야 하네
enumerate로 순서 같이 먹여놓자
'''

N = int(input())
balloon = list(map(int,input().split()))
balloon = [(i,idx) for idx, i in enumerate(balloon)]
ans = []
current_index = 0
#풍선 1번에 나온 숫자만큼 이동하고 풍선1번 삭제, 반복 얼마나? 최대 N번
for i in range(N):
    ans.append((balloon[current_index][1])+1)
    val,id = balloon.pop(current_index)
    current_index += val

for i in ans:
    print(i,end=' ')