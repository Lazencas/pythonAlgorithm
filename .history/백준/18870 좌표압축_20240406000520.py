'''
자기보다 작은 숫자의 개수가 곧 자기의 수.
이걸 오름차순 정렬하면 0번 인덱스는 자기보다 작은 수가 없으므로 0,
1번인덱스는 자기보다 작은 수가 0번인덱스 1개, 
2번인덱스는 자기보다 작은 수가 0번,1번 ....
이런식으로 인덱스의 숫자가 곧 자기보다 작은 숫자의 개수가 되는 것을 알 수 있다.

그래서 중복을 제거하고 정렬한 새로운 리스트를 만들고
새로만든 리스트의 인덱스 번호를
'''
import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int,input().split()))
x2 = sorted(list(set(x)))
#x2의 값을 키 값으로 하고, 밸류 값으로는 인덱스를 넣어준다
dic = {x2[i] : i for i in range(len(x2))}
for i in x:
    #출력할 때 해당 값으로 딕셔너리 조회
    print(dic[i],end=' ')