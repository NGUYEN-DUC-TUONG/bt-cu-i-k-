class Solution:
    def TamGiacDuoi(matrix):
        n = len(matrix)
        
        # Kiểm tra từng phần tử nằm trên đường chéo chính và phần tử nằm phía trên đường chéo chính
        for i in range(n):
            for j in range(i + 1, n):
                if matrix[i][j] != 0:
                    return False
        return True


# Nhập ma trận vuông từ người dùng
n = int(input("Nhập kích thước ma trận vuông: "))
matrix = []
print("Nhập ma trận:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print("Mảng là ma trận tam giác dưới:", Solution.TamGiacDuoi(matrix))