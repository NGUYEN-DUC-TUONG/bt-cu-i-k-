def Mang_TrungHang(matrix):
    n = len(matrix)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if matrix[i] == matrix[j]:
                return True
    return False

def nhap_ma_tran():
    matrix = []
    n = int(input("Nhập số hàng/cột của ma trận: "))
    print("Nhập ma trận:")
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

# Nhập ma trận từ người dùng và kiểm tra
matrix = nhap_ma_tran()
print("Ma trận vừa nhập:")
for row in matrix:
    print(row)
print("Ma trận có ít nhất hai hàng giống nhau:", Mang_TrungHang(matrix))