def Hieu(a, b):
    # Sử dụng tập hợp để tìm các phần tử chỉ có trong a mà không có trong b
    unique_a = set(a)
    unique_b = set(b)
    
    difference = unique_a - unique_b
    # Sắp xếp kết quả theo thứ tự tăng dần
    result = sorted(difference)
    
    return result
# Ví dụ minh họa
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

print("Mảng a:", a)
print("Mảng b:", b)

c = Hieu(a, b)
print("Kết quả:", c)