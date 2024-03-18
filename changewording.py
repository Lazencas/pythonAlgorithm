# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 
# ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 
# 같이 4단계를 거쳐 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 
# 하도록 solution 함수를 작성해주세요.
# def solution(begin, target, words):
#     answer = 0
#     #알파벳 한개를 뺀 나머지 알파벳이 값이 같은 단어가 있는지 확인.
#     #없으면 0리턴, 있으면 그걸로 변경하고  변경한 단어가 target단어랑 같은 단어인지 확인
    
#     #target이 주어진 리스트에 없으면 바로 0 반환
#     if target not in words:
#         return answer
    
#     begin = list(begin)
#     target = list(target)
#     #단어길이 미리 변수에 저장해두기
#     word_len = len(begin)
#     #우선 주어진 단어를 다 쪼개서 이차원배열에 아스키값으로 저장해야겠다.? 근데 굳이 아스키값으로 바꿀 필요가있나?;;
#     my_words  = list(map(list,words))
#     # for i in my_words:
#     #     print(i)
#     # 전체 words의 크기만큼 + begin 크기 + begin크기만큼 words, count가 단어길이-1이면 그 단어로 변경하면 됨 그리고 변경된 단어를 타겟이랑 비교해서
#     #같으면 리턴, 다르면 다시 반복
#     for i in range(len(my_words)):
#         equal_count = 0
#         for j in range(len(my_words[0])):
#             if begin[j] == my_words[i][j]:
#                 equal_count += 1
#         if equal_count == word_len-1:
#             begin = my_words[i]
#             print(begin)
#             #여기에서 begin이랑 target비교하면 되겠다.
#             tmp=0
#             for k in range(len(begin)):
#                 if begin[k] == target[k]:
#                     tmp +=1
#             if tmp == word_len-1:
#                 answer +=2
#                 return answer
#             answer += 1   
#     #target이랑 한 글자 차이나는지 따지고 한글자만 차이나면 바로 answer에 +1 하고 리턴하자
#     #아마 부분적으로 두개 같은단어가 두개 이상일때 둘중 뭘 선택할지 로직이 필요할거같음
    
    
#     return answer

def bfs(begin,target,words):
    need_checked = list()
    need_checked.append([begin,0])

    while need_checked:
        current_word, count = need_checked.pop(0)
        
        if current_word == target:
            answer = count
            return answer
        
        for word in words:
            tmp =0
            for i in range(len(current_word)):
                if word[i] != current_word[i]:
                    tmp+=1

            if tmp == 1:
                need_checked.append([word,count+1])   
                    
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    answer = bfs(begin,target,words)
    return answer




begin = 'hit'
target = 'cog'
target2 = 'kok'
words= ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = 	["hot", "dot", "dog", "lot", "log"]
words3 = ["hot", "hoc", "hok", "kok"]
print(solution(begin,target2,words3))