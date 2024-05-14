def nhap_mang():
    n = int(input("Nhập số phần tử của mảng: "))
    mang = []
    for i in range(n):
        phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
        mang.append(phan_tu)
    return mang

def DayConDauTien(a, b):
    # Tạo một tập hợp lưu trữ các dãy con của a
    a_set = set()
    # Duyệt qua từng phần tử của a để tạo dãy con
    for i in range(len(a)):
        for j in range(i, len(a)):
            # Thêm dãy con vào tập hợp
            a_set.add(tuple(a[i:j+1]))

    # Duyệt qua từng phần tử của b để kiểm tra xem có dãy con nào trong tập hợp của a không
    for i in range(len(b)):
        for j in range(i, len(b)):
            # Kiểm tra xem dãy con của b có trong tập hợp của a không
            if tuple(b[i:j+1]) in a_set:
                return list(tuple(b[i:j+1]))  # Trả về dãy con đầu tiên được tìm thấy
    
    # Nếu không tìm thấy dãy con nào chung, trả về một danh sách rỗng
    return []

# Nhập mảng a 
print("Nhập mảng a:")
a = nhap_mang()

# Nhập mảng b 
print("Nhập mảng b:")
b = nhap_mang()

print("Dãy con chung đầu tiên:", DayConDauTien(a, b))