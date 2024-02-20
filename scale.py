# 문제
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다.
#  c는 1로, d는 2로, ..., C를 8로 바꾼다.

# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

def scale(scale_list):
#반환할 정답이 들어있는 변수
    answer = ""
    list = scale_list
    #correct가 7이면 ascending
    correct = 0
    #decorrect가 7이면 decending
    decorrect= 0
#1부터 8까지 오름차순인지 확인해서 맞다면 ascending반환
    for idx in range(7):
        if list[idx]+1 == list[idx+1]:
            correct += 1 

#8부터 1까지 내림차순이면 descending
    for idx in range(7):
        if list[idx]-1 == list[idx+1]:
            decorrect += 1 

#그 외의 조건은 mixed
    if correct == 7:
        answer="ascending"

    elif decorrect == 7:
        answer="decending"

    else:
        answer="mixed"


    return answer

scale_list = [1,2,3,4,5,6,7,8]
de_list = [8,7,6,5,4,3,2,1]
mix_list = [2,5,1,3,4,6,7,8]
print(scale(mix_list))