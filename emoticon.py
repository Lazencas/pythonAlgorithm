def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []

    # 이모티콘 할인율 구하기
    #문제1. 어떻게 할인의 모든 경우의 수를 따질것인가?
    #4중반복문?

    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d

    dfs([0] * len(emoticons), 0)

    # for i in range(256):
    #     for j in range(192):
    #         for k in range(128):
    #             for l in range(64):
    #                 if i//64 ....
    
    for d in range(len(discount)):
        plus_user = 0
        profit = 0

        for user in users:
            emoticon_buy = 0
            for i in range(len(emoticons)):
                if discount[d][i] >= user[0]:
                    emoticon_buy += emoticons[i] * ((100 - discount[d][i]) / 100)
            if user[1] <= emoticon_buy:
                plus_user += 1
            else:
                profit += emoticon_buy

        if answer[0] < plus_user:
            answer = [plus_user, int(profit)]
        elif answer[0] == plus_user:
            if answer[1] < profit:
                answer = [plus_user, int(profit)]

    return answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))