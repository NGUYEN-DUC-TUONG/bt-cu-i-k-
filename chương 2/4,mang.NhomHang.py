def NhomHang(matrix):
    n = len(matrix)
    groups = {}
    for i in range(n):
        row = matrix[i]
        row_str = ','.join(map(str, row))
        if row_str not in groups:
            groups[row_str] = []
        groups[row_str].append(i)

    for group in groups.values():
        if len(group) > 1:
            print("Nhóm hàng giống nhau:", group)
            
def nhap_ma_tran():
    matrix = []
    while True:
        row_input = input("Nhập hàng mới (nhập 'q' để kết thúc): ")
        if row_input.lower() == 'q':
            break
        row = list(map(int, row_input.split()))
        matrix.append(row)
    return matrix

# Ví dụ sử dụng
matrix = nhap_ma_tran()
print("Ma trận:")
for row in matrix:
    print(row)

print("\nCác nhóm hàng giống nhau:")
NhomHang(matrix)