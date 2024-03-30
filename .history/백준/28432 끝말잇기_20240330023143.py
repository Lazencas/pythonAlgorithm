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

target_index = words.index('?')
target_list = []
#? 앞의 문자
target_list[0] = words[target_index-1]
#? 뒤 문자
target_list[1] = words[target_index+1]

for word in candi:
    if word[0]==target_list[0][-1] and word[-1]==target_list[1][0]:
        print(word)
        break