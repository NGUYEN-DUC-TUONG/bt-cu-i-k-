def Giao(a, b):
    # Sử dụng tập hợp để tìm các phần tử xuất hiện trong cả a và b
    set_a = set(a)
    set_b = set(b)
    
    intersection = set_a.intersection(set_b)
    # Sắp xếp kết quả theo thứ tự tăng dần
    result = sorted(intersection)
    
    return result
# Ví dụ minh họa
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

print("Mảng a:", a)
print("Mảng b:", b)

c = Giao(a, b)
print("Kết quả:", c)