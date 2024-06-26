# 1+ = { 1, 11, 111, 1111, 11111, … }
# 10+ = { 10, 100, 1000, 10000, 100000, … }
# (01)+ = { 01, 0101, 010101, 01010101, 0101010101, … }
# (1001)+ = { 1001, 10011001, 100110011001, … }
# 10+11 = { 1011, 10011, 100011, 1000011, 10000011, … }
# (10+1)+ = { 101, 1001, 10001, 1011001, 1001101, 100011011000001, … }

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 전파를 표현하는, {
#      0, 1 }만으로 이루어진 문자열이 공백 없이 주어진다. 문자열 길이는 (1 ≤ N ≤ 200)의 범위를 갖는다.

# 출력
# 각 테스트 케이스에 대해 주어진 전파가 문제에서 제시한 패턴이면 “YES”를 그렇지 않은 경우는 “NO”를 출력한다. 
# 출력 문자열은 모두 대문자로 구성되어 있다.
import re
for i in range(int(input())):
    S=input()
    P = re.compile('(100+1+|01)+')
    if P.fullmatch(S):
        print('YES')
    else:
        print('NO')