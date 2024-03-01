# 문제
# 여러분도 알다시피 여러분의 프린터 기기는 여러분이 
# 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 
# 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 
# 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 
# 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 
# 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, 
# A문서는 3번째로 인쇄되게 된다.

# 입력
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 출력
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

testcase = int(input())
answer_file_order = 0
anlist = []
repeat = True

#입력된 테스트 케이스 수 만큼 반복
for i in range(testcase):
    file_ea, answer_file_location = map(int,input().split(' '))
    print_q = list(map(int,input().split(' ')))
    #프린트큐 전체에서 가장 큰 수를 찾는다
    #프린트큐를 전체 순회하면서 가장 큰수보다 작은 수가 있으면 [0]번째 에서 빼서 [-1]번째에 넣어준다
    #이렇게해서 내림차순이 완료 될때까지 반복한다.
    #자리 옮겨지는데 목적으로 하는 문서가 어디로 옮겨졋는지 자리를 어떻게 찾지?
    #똑같은 크기의 0으로 채워진 리스트를 만들고 목표 문서의 위치 인덱스에 1을 주고 프린트큐랑 동기화
    #찾을때는 리스트에서 값이1인 거 찾고 그 인덱스 반환하면 그게 답
    #가장큰수와 가장 작은수를 일단 찾을 수 있다. max(print_queue), min(print_queue)
    #answer_file의 어떤 정보를 기억해야할거같은데, answer_file의 값-1 만큼의 위치의 print_queue가 우선순위고
    #이거 answer_file_priority 라고.... 언제까지 정렬을 반복할지랑..... 어떻게 정렬할지...... 이거 두개만 해결하면 된다
    #정렬확인로직, 정렬로직
    #10분고민....
    #이걸로 정답파일의 위치를 추적
    anlist = [0 for i in range(file_ea)]
    anlist[answer_file_location] = 1
    maxnum = max(print_q)
    temp_q = [i for i in print_q]

    #내림차순 정렬 정답 구하는 로직
    for i in print_q:
        if i == 9:
            temp_q[i]=9
        if i == 8:
            temp_q[i]=8
        if i == 7:
            temp_q[i]=7                    
        if i == 6:
            temp_q[i]=6
        if i == 5:
            temp_q[i]=5
        if i == 4:
            temp_q[i]=4
        if i == 3:
            temp_q[i]=3
        if i == 2:
            temp_q[i]=2
        if i == 1:
            temp_q[i]=1




    #우선순위 따라 정렬하는 로직
    for idx in range(file_ea-1):
        if temp_q[idx] < maxnum:
            anlist.append(anlist.pop(0))
        
    while repeat:
