def solution(book_time):
    answer = 1
    
    def min(str):
        hour, minute = map(int, str.split(':'))
        return hour*60 + minute
    
    books = sorted([[min(i[0]), min(i[1])+10] for i in book_time])
    rooms=[[0,0]]
    
    #최대로 겹치는 시간의 방 개수를 세면 될거 같은데, 아니면 전체에서 줄여나가는 식으로?
    for bookin, bookout in books:
        for i in range(len(rooms)):
            if rooms[i][1]>=bookin:
                rooms.append([bookin,bookout])
            else:
                rooms[i] = [bookin,bookout]
    
    answer = len(rooms)
    
    return answer

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

print(solution(book_time))