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
dic = {x2[i] : i for i in range(len(x2))}
print(dic)
for i in x:
    print(dic[i],end=' ')