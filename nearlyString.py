def solution(s):
    answer = []
    #문자열 돌면서 각 문자의 위치 찾고 문자가 리스트에 있는지 확인, 없다면 해당 문자를 다른리스트에 추가 -1
    #문자가 리스트에 있다면..... 리스트 저장할때 인덱스 번호 같이 넣어주자 그거 기반으로 처리
    checked = []
    location= []
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] not in checked:
            checked.append(s_list[i])
            location.append(i)
            answer.append(-1)
        else:
            #앞에 나온거랑 거리 따져서 반환하는 로직
            tmp = []
            for j in range(i):
                if s_list[j] == s_list[i]:
                    rest_list = list(filter(lambda x :s_list[x]==s_list[j],range(len(s_list))))
                    rest_list = max(rest_list)
                    location.append(i)
                    checked.append(s_list[i])
                    answer.append(i-rest_list)
                    break
    return answer
s = "banana"
print(solution(s))