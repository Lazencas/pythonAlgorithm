a = [[1,2], [4,5], [8,9]]
b = [[i]*3 for i in range(1)]

c = [list(i) for i in zip(*a)]


re = [[0]*3 for i in range(2)]


for i in range(2):
    for j in range(3):
        re[i][j] = a[j][i]

nemo = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(arr):
    n = len(arr)
    rotated_arr = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_arr[j][n-1-i] = arr[i][j]
    return rotated_arr

def rerotate(arr):
    n = len(arr)
    rerotated_arr = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            rerotated_arr[n-1-j][i] = arr[i][j]
    return rerotated_arr

print(rotate(nemo))