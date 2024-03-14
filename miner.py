def solution(picks, minerals):
    answer = 0
    #각 광물의 값을 dia 25, iron 5, stone 1로 설정하고 인접한 5개의 배열의 합이 가장 큰곳에는 가장
    #좋은 곡괭이를 쓰면 될거같다. 그리고 곡괭이는 가장좋은것부터 안좋은순으로 사용해야 최소 피로도로 광물캘수 있을거같음
    #각 0~4번 인덱스, 5~ 9번, 10~ 14번인덱스 이런식으로 5개씩 끊어서 배열로 만들어서 따지면 될듯
    #5개씩 어떻게 자르지?
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks)*5]
        
    count_minerals = [[0,0,0]for _ in range(len(minerals)) ]
    
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            count_minerals[i//5][0]+=1
        elif minerals[i]=='iron':
            count_minerals[i//5][1]+=1
        elif minerals[i]=='stone':
            count_minerals[i//5][2]+=1
            
    count_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    for mineral in count_minerals:
        if picks[0] > 0:
            picks[0] -= 1
            answer+=(mineral[0]+mineral[1]+mineral[2])
            
        elif picks[1] > 0:
            picks[1] -= 1
            answer += (mineral[0]*5 + mineral[1] + mineral[2])
            
        elif picks[2] > 0:
            picks[2] -= 1
            answer += (mineral[0]*25 + mineral[1]*5 + mineral[2])
            
    return answer

    
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))