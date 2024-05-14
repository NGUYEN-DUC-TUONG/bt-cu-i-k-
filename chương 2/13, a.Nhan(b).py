class Solution:
    def Nhan(a, b):
        # Kiểm tra dấu của a và b
        sign = a[0] ^ b[0]
        
        # Tính toán giá trị tuyệt đối của a và b
        positive_a = [abs(x) for x in a[1:]]
        positive_b = [abs(x) for x in b[1:]]
        
        # Tính tích của hai số
        result = [0] * (len(positive_a) + len(positive_b))
        for i in range(len(positive_a)):
            for j in range(len(positive_b)):
                result[i + j] += positive_a[i] * positive_b[j]
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Xác định dấu của kết quả
        result_sign = 0 if result == [0] else sign
        
        # Xóa các số 0 không cần thiết ở đầu kết quả
        while result and result[-1] == 0:
            result.pop()
        
        # Nếu kết quả bị tràn, trả về [-1]
        if result and len(result) > 9:
            return [-1]
        
        # Thêm dấu vào kết quả
        return [result_sign] + result

# Nhập số a và b 
a = list(map(int, input("Nhập số a (âm: 1, không âm: 0), sau đó nhập số: ").split()))
b = list(map(int, input("Nhập số b (âm: 1, không âm: 0), sau đó nhập số: ").split()))

result = Solution.Nhan(a, b)
print("Kết quả của a * b:", result)