N = int(input())
words = []
candi = []
for i in range(N):
    w = input()
    words.append(w)

N2= int(input())
for j in range(N2):
    w = input()
    if w not in words:
        candi.append(w)
target_list = []
target_index = words.index('?')

if target_index == 0:
    target_list.append(words[target_index+1])
    for word in candi:
        #?가 처음에 있는경우
        if word[-1]==target_list[0][0]:
            print(word)
            break

elif target_index==len(words)-1:
    target_list.append(words[target_index-1])
    for word in candi:
        #?가 마지막에 있는 경우
        if word[0]==target_list[0][-1]:
            print(word)
            break

else:
    #? 앞의 문자
    target_list.append(words[target_index-1])
    #? 뒤 문자
    target_list.append(words[target_index+1])
    for word in candi:
        if word[0]==target_list[0][-1] and word[-1]==target_list[1][0]:
            print(word)
            break