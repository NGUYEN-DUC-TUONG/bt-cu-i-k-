class Solution:
    def Cong(a, b):
        # Độ dài của số nguyên không dấu lớn nhất có thể lưu trữ trong một phần tử list
        MAX_DIGIT = 10
        
        # Chuyển đổi mảng số nguyên thành chuỗi và nghịch đảo
        str_a = ''.join(map(str, a[::-1]))
        str_b = ''.join(map(str, b[::-1]))
        
        # Thực hiện phép cộng
        result = int(str_a) + int(str_b)
        
        # Kiểm tra xem kết quả có bị tràn không
        if result >= 10 ** MAX_DIGIT:
            return [-1] * MAX_DIGIT
        
        # Chuyển đổi kết quả thành mảng số nguyên và nghịch đảo
        result_list = list(map(int, str(result).zfill(MAX_DIGIT)[::-1]))
        return result_list

# Nhập mảng a
a = list(map(int, input("Nhập mảng số nguyên a: ").split()))
# Nhập mảng b
b = list(map(int, input("Nhập mảng số nguyên b: ").split()))
print("Kết quả phép cộng:", Solution.Cong(a, b))