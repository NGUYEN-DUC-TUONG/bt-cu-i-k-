def DayConDaiNhat(a, b):
    # Tạo một tập hợp lưu trữ các dãy con của a
    a_set = set()
    # Biến lưu trữ chiều dài lớn nhất của dãy con chung
    max_length = 0
    # Duyệt qua từng phần tử của a để tạo dãy con
    for i in range(len(a)):
        for j in range(i, len(a)):
            # Tính chiều dài của dãy con
            length = j - i + 1
            # Thêm dãy con vào tập hợp
            a_set.add(tuple(a[i:j+1]))
            # Kiểm tra xem dãy con có trong b không và có dài hơn dãy con lớn nhất đã tìm được không
            if tuple(a[i:j+1]) in set(b) and length > max_length:
                max_length = length

    # Duyệt qua từng phần tử của b để kiểm tra xem có dãy con nào trong tập hợp của a không
    for i in range(len(b)):
        for j in range(i, len(b)):
            # Tính chiều dài của dãy con
            length = j - i + 1
            # Kiểm tra xem dãy con của b có trong tập hợp của a không và có dài hơn dãy con lớn nhất đã tìm được không
            if tuple(b[i:j+1]) in a_set and length > max_length:
                max_length = length
                # Lấy dãy con có chiều dài lớn nhất
                max_length_subsequence = b[i:j+1]

    return list(max_length_subsequence)

# Nhập mảng a 
print("Nhập mảng a:")
a = list(map(int, input().split(',')))

# Nhập mảng b 
print("Nhập mảng b:")
b = list(map(int, input().split(',')))

print("Dãy con có chiều dài lớn nhất:", DayConDaiNhat(a, b))
