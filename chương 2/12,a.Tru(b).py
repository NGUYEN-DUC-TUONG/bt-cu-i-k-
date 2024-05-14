class Solution:
    def Tru(a, b):
        # Chuyển đổi số âm thành số dương bằng cách đảo bit dấu
        def to_positive(num):
            return [num[i] & 0x7FFFFFFF for i in range(len(num))]
        
        # Tạo mảng đại diện cho số âm và số dương
        positive_a = a[1:]
        positive_b = b[1:]
        
        # Nếu a là số âm, chuyển đổi thành số dương
        if a[0] == 1:
            positive_a = to_positive(positive_a)
        
        # Nếu b là số âm, chuyển đổi thành số dương
        if b[0] == 1:
            positive_b = to_positive(positive_b)
        
        # Kiểm tra xem a >= b không, nếu không, trả về [0] đại diện cho kết quả bằng 0
        if positive_a < positive_b:
            return [0]
        
        # Tính hiệu của hai số
        result = [x - y for x, y in zip(positive_a, positive_b)]
        
        # Nếu kết quả rỗng hoặc kết quả không bị tràn, trả về kết quả
        if not result or result[0] < 0:
            return [-1]
        
        return result

# Nhập số a và b 
a = list(map(int, input("Nhập số a (âm: 1, không âm: 0), sau đó nhập số: ").split()))
b = list(map(int, input("Nhập số b (âm: 1, không âm: 0), sau đó nhập số: ").split()))

result = Solution.Tru(a, b)
print("Kết quả của a - b:", result)
