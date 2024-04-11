'''
board 에서 moves를 보고 인형을 뽑아서 stack에 넣는함수
넣고나서 stack을 체크해서 인형 중복처리 하는 함수 < 중복처리시 카운트
moves를 모두 실행하고 나면 카운트값 반환
moves의 값 -1 = 실제 board의 인덱스 값

'''

def solution(board, moves):
    answer = 0
    doll_stack = []
    #인형을 뽑아서 stack에 넣는 함수
    def pickup(moves_value):
        
        idx = moves_value-1
        for i in range(len(board)):
            if board[i][idx] != 0:
                doll_stack.append(board[i][idx])
                board[i][idx] = 0
                break
        print('board체크',board)
        print('stack체크',doll_stack)
    #stack을 체크하고 중복을 처리하는 함수, pickup 함수가 실행되면 항상
    #뒤따라서 실행되어야함
    def check(answer):
        if len(doll_stack)>=2:
            if doll_stack[-1]==doll_stack[-2]:
                answer+=1
                doll_stack.pop()
                doll_stack.pop()
    
    for i in moves:
        pickup(i)
        answer = check(answer)

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))