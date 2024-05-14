class Solution:
    def NhomCot(matrix):
        n = len(matrix)
        
        # Tạo một từ điển để lưu số lần xuất hiện của mỗi cột
        col_count = {}
        for i in range(n):
            for j in range(n):
                if j in col_count:
                    col_count[j][matrix[i][j]] = col_count[j].get(matrix[i][j], 0) + 1
                else:
                    col_count[j] = {matrix[i][j]: 1}
        
        # In ra nhóm chỉ mục cột của các cột giống nhau
        for col, counts in col_count.items():
            if max(counts.values()) >= 2:
                print("Nhóm cột giống nhau:", col)
                for value, count in counts.items():
                    if count >= 2:
                        print(f"- Giá trị {value} xuất hiện {count} lần trong cột {col}")

# Nhập ma trận vuông từ người dùng
n = int(input("Nhập kích thước ma trận vuông: "))
matrix = []
print("Nhập ma trận:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print("\nCác nhóm chỉ mục cột của các cột giống nhau:")
Solution.NhomCot(matrix)