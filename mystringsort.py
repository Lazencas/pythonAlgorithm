def solution(strings, n):
    strings.sort(key=lambda x:x[n])
    for i in range(len(strings)-1):
        if strings[i][n] == strings[i+1][n]:
            for j in range(len(strings[i])):
                if ord(strings[i][j]) > ord(strings[i+1][j]):
                    strings[i],strings[i+1]= strings[i+1],strings[i]
    return strings

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))