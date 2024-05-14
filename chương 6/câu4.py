def Hop(a, b):
    # Kết hợp các phần tử từ cả hai mảng
    combined = a + b
    
    # Loại bỏ các phần tử trùng lặp và sắp xếp kết quả theo thứ tự tăng dần
    result = sorted(set(combined))
    
    return result
# Ví dụ minh họa
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

print("Mảng a:", a)
print("Mảng b:", b)

c = Hop(a, b)
print("Kết quả:", c)