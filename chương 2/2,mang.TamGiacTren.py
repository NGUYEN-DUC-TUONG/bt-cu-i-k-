def Mang_TamGiacTren(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True

# Ví dụ 
# Ma trận vuông tam giác trên
matrix1 = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]

# Ma trận vuông không phải tam giác trên
matrix2 = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

print("matrix1 là ma trận tam giác trên:", Mang_TamGiacTren(matrix1))
print("matrix2 là ma trận tam giác trên:", Mang_TamGiacTren(matrix2))
