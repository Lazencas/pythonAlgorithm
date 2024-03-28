# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
#  단, 대문자와 소문자를 구분하지 않는다. #대문자 알파벳 A~Z 아스키 코드값으로 65~90
S = input()
S = S.upper()
alpha = list(set(S))
count = [0 for i in range(len(alpha))]
for i in range(len(alpha)):
    for j in S:
        if alpha[i]==j:
            count[i]+=1
if count.count(max(count)) > 1:
    print('?')
else:
    print(alpha[count.index(max(count))])
    

