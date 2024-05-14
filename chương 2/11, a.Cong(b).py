class Solution:
    def Cong(a, b):
        # Chuyển đổi số âm thành số dương bằng cách đảo bit dấu
        def to_positive(num):
            return [num[i] & 0x7FFFFFFF for i in range(len(num))]
        
        # Tạo mảng đại diện cho số âm và số dương
        positive_a = a[1:]
        positive_b = b[1:]
        
        # Nếu a hoặc b âm, chuyển đổi thành số dương
        if a[0] == 1:
            positive_a = to_positive(positive_a)
        if b[0] == 1:
            positive_b = to_positive(positive_b)
        
        # Tính tổng của hai số
        total = [x + y for x, y in zip(positive_a, positive_b)]
        
        # Nếu tổng vượt quá giới hạn, trả về mảng các số -1
        if any(x > 0x7FFFFFFF for x in total):
            return [-1]
        
        # Nếu a và b cùng dấu, kết quả giữ nguyên dấu
        if a[0] == b[0]:
            return [a[0]] + total
        else:  # Nếu a và b khác dấu, kiểm tra kết quả
            if sum(total) == 0:
                return [0]  # Nếu kết quả là 0, trả về số dương 0
            else:
                return [1] + total  # Nếu kết quả không phải 0, trả về số âm
            
# Nhập số a và b 
a = list(map(int, input("Nhập số a (âm: 1, không âm: 0), sau đó nhập số: ").split()))
b = list(map(int, input("Nhập số b (âm: 1, không âm: 0), sau đó nhập số: ").split()))

result = Solution.Cong(a, b)
print("Kết quả của a + b:", result)