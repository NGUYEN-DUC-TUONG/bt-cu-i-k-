def Duynhat(a):
    # Sử dụng tập hợp để loại bỏ các phần tử trùng lặp
    unique_numbers = set(a)
    
    # Sắp xếp các số duy nhất theo thứ tự tăng dần
    sorted_unique_numbers = sorted(unique_numbers)
    
    # Chuyển kết quả từ tập hợp thành mảng
    result = list(sorted_unique_numbers)
    
    return result

# Ví dụ minh họa
a = [1, 5, 3, 7, 5, 9, 7]
print("Mảng ban đầu:", a)

b = Duynhat(a)
print("Mảng duy nhất và sắp xếp:", b)