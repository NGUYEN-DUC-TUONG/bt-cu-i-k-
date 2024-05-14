class Solution:
    def TrungCot(matrix):
        n = len(matrix)
        
        # Tạo một từ điển để lưu số lần xuất hiện của mỗi cột
        col_count = {}
        for i in range(n):
            for j in range(n):
                if j in col_count:
                    col_count[j][matrix[i][j]] = col_count[j].get(matrix[i][j], 0) + 1
                else:
                    col_count[j] = {matrix[i][j]: 1}
        
        # Kiểm tra xem có cột nào xuất hiện ít nhất 2 lần không
        for col in col_count.values():
            if max(col.values()) >= 2:
                return True
        return False


# Nhập ma trận vuông từ người dùng
n = int(input("Nhập kích thước ma trận vuông: "))
matrix = []
print("Nhập ma trận:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print("Mảng có ít nhất hai cột giống nhau:", Solution.TrungCot(matrix))