# 문제
# 센티는 마법 도구들을 지니고 여행을 떠나는 것이 취미인 악당이다.

# 거인의 나라에 도착한 센티는 자신보다 키가 크거나 같은 거인들이 있다는 사실이 마음에 
# 들지 않았다.

# 센티가 꺼내 들은 마법 도구는 바로 마법의 뿅망치로, 이 뿅망치에 맞은 사람의 키가 ⌊ 뿅망치에
#  맞은 사람의 키 / 2 ⌋로 변하는 마법 도구이다.
#   단, 키가 1인 경우 더 줄어들 수가 없어 뿅망치의 영향을 받지 않는다.

# 하지만 마법의 뿅망치는 횟수 제한이 있다. 그래서 센티는 마법의 뿅망치를 효율적으로 사용하기
#  위한 전략을 수립했다.
#   바로 매번 가장 키가 큰 거인 가운데 하나를 때리는 것이다.

# 과연 센티가 수립한 전략에 맞게 마법의 뿅망치를 이용한다면 거인의 나라의 
# 모든 거인이 센티보다 키가 작도록 할 수 있을까?

# 입력
# 첫 번째 줄에는 센티를 제외한 거인의 나라의 인구수 N (1 ≤ N ≤ 105)과 센티의 
# 키를 나타내는 정수 Hcenti (1 ≤ Hcenti ≤ 2 × 109), 
# 마법의 뿅망치의 횟수 제한 T (1 ≤ T ≤ 105)가 빈칸을 사이에 두고 주어진다. 

# 두 번째 줄부터 N개의 줄에 각 거인의 키를 나타내는 정수 H (1 ≤ H ≤ 2 × 109)가 주어진다.

# 출력
# 마법의 뿅망치를 센티의 전략대로 이용하여 거인의 나라의 모든 거인이 센티보다 키가 
# 작도록 할 수 있는 경우, 첫 번째 줄에 YES를 출력하고, 두 번째 줄에 마법의 뿅망치를 
# 최소로 사용한 횟수를 출력한다.

# 마법의 뿅망치를 센티의 전략대로 남은 횟수 전부 이용하고도 거인의 나라에서 센티보다 
# 키가 크거나 같은 거인이 있는 경우, 첫 번째 줄에 NO를 출력하고, 두 번째 줄에 마법의 
# 뿅망치 사용 이후 거인의 나라에서 키가 가장 큰 거인의 키를 출력한다.
'''
시간제한 1초, 메모리 1기가
최대입력  10만, 10억, 10만

모든 거인을 센티보다 작게 할 수 있는지랑, 제일 큰 거인
제일큰 이니까 이진탐색인가? 근데 이진탐색인거 같다.

입력값 큰 거 + 제일 큰 거인 = 이진탐색? XX
그냥 큰거 계속 뽑는 식이니 힙이다.

가장 키가 큰 거인을 찾아서 반으로 줄이고, 그 다음 큰 거인 찾아서 반으로 줄이고
T번 반복하고, 가장 큰 거인을 마지막으로 출력


'''
from heapq import *
import sys
input = sys.stdin.readline
N, Hc, T = map(int,input().split())
giants = []
heapify(giants)
for i in range(N):
    h = int(input())
    heappush(giants,-h)

for i in range(T):
    g = -(heappop(giants))//2
    heappush(giants,-g)
print(giants)


