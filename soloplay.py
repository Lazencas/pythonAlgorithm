
def solution(cards):
    answer = []
    #몇번만에 열어본상자까지 
    for i in range(len(cards)):
        tmp = 0
        while cards[i]:
            next_i = cards[i]-1
            cards[i], i=0, next_i
            tmp+=1
        answer.append(tmp)
    answer.sort()
    
    return answer[-1]*answer[-2]


cards = [8,6,3,7,2,5,1,4]

print(solution(cards))