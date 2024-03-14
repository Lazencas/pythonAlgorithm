def solution(book_time):
    answer = 1
    
    def min(str):
        hour, minute = map(int, str.split(':'))
        return hour*60 + minute
    
    books = sorted([[min(i[0]), min(i[1])+10] for i in book_time])
    rooms=[[0,0]]
    
    chk = 0
    #최대로 겹치는 시간의 방 개수를 세면 될거 같은데, 아니면 전체에서 줄여나가는 식으로?
    for bookin, bookout in books:
        for i in range(len(rooms)):
            if rooms[i][1]>bookin:
                chk+=1
            else:
                chk = 0
                rooms[i] = [bookin,bookout]
                break

        if chk >= 1 :
            rooms.append([bookin,bookout])
            chk = 0

    answer = len(rooms)
    
    return answer

book_time = [["09:10", "10:10"], ["10:20", "12:20"]]

print(solution(book_time))