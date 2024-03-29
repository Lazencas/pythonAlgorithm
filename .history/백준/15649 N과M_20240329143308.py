# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며,
#  각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
import sys
from itertools import *
input = sys.stdin.readline
N, M = map(int,input().split())
N_list = [i+1 for i in range(N)]
ans = combinations(N_list,M)
ans = list(set(ans))
# ans = list(map(list,ans))
ans.sort()
ans = list(map(str,ans))
for i in ans:
    print(i)
    print(' '.join(list(i))) 