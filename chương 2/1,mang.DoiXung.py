def Mang_DoiXung(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Ví dụ 
# Ma trận vuông đối xứng
matrix1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

# Ma trận vuông không đối xứng
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("matrix1 là ma trận đối xứng:", Mang_DoiXung(matrix1))
print("matrix2 là ma trận đối xứng:", Mang_DoiXung(matrix2))