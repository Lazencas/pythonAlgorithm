# 문제
# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는,
# 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다
# 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 
# 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

# 출력
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 
# 한 경우에는 0을 출력하면 된다.
'''
입력 받아서 0이면 힙팝으로 프린트 출력하고, 아니면 그냥 값 밀어넣으면 끝아닌가?
그리고 갑 없을 때, 0이면 0출력

근데 절대값으로 계산해야하는데..... 
값 넣을때 heap을 2개 만들어서 +랑 - 따로 관리하자
뺄 때 -는 제일 큰 거, +는 제일 작은거 절대 값 비교해서 출력
두개 다 크기 0이면 0출력
'''
import sys
from heapq import *
input = sys.stdin.readline
plus = []
minus = []
heapify(plus)
heapify(minus)
N = int(input())
for i in range(N):
    x = int(input())
    if x != 0:
        if x > 0:
            heappush(plus,x)
        else:
            heappush(minus,-(x))
    else:
        #절대값 가장 작은 거 출력하는 로직
        #두개의 힙이 다 비어있을 때
        if len(plus) == 0 and len(minus) ==0:
            print(0)
            continue
        #플러스 힙만 있을 때
        elif len(plus) != 0 and len(minus) == 0:
            print(heappop(plus))
        #마이너스 힙만 있을 때
        elif len(minus) !=0 and len(plus)==0:
            print(-(heappop(minus)))

        else:
            #둘다 힙이 안비어 있을 때
            #플러스 힙이 더 작을 때
            if plus[0] < minus[0]:
                print(heappop(plus))
            #마이너스 힙이 더 작을 때
            elif minus[0] < plus[0]:
                print(-(heappop(minus)))
            #둘의 힙이 같을 때는 더 작은 값인 마이너스 힙이 먼저
            else:
                print(-(heappop(minus)))

 
