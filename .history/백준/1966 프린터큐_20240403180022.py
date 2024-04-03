# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 입력
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고,
# 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 출력
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
'''
max값이 나올때 까지 리스트의 앞에서 빼서 새로 리스트 만들기1234>2341>3412>4123>231>312>12>21>1
근데 처음 리스트에서 타겟의 인덱스를 기억해놔야 함. 출력리스트 바뀌면 순서도 바꿔줘야하나?; < 이걸 순서로 기억해서 개수세네
enumaerate 사용

데이터의 개수가 최대 100개 이하 이므로 그대로 구현하면 됨
현재 리스트에서 가장 큰 수가 앞에 올 때까지 회전시킨뒤에 추출
가장 큰 수가 M이면서 가장 앞에 있을 때 프로그램 종료

'''
tc = int(input())
for i in range(tc):
    N, target_index = list(map(int,(input().split())))
    sequence = list(map(int,input().split()))

    sequence = [(i,idx) for idx,i in enumerate(sequence)]

    cnt=0
    while True:
        if sequence[0][0] == max(sequence, key=lambda x:x[0])[0]:
            cnt+=1
            if sequence[0][1]==target_index:
                print(cnt)
                break
            else:
                sequence.pop(0)
        else:
            sequence.append(sequence.pop(0))